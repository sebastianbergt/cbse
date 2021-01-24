import sha256
from enum import Enum
from pathlib import Path
from re import match
import cbse.cpp


class ReqType(Enum):
    BASIC = 1

# Requirement


class Req:
    def __init__(self, id, text: str, req_type: ReqType, trace_filepath: Path = None, trace_function: str = None, function_hash: str = None):
        self.id = id
        self.text = text
        self.text_hash = sha256.sha256(str.encode(text))
        self.type = req_type
        self.trace_filepath = trace_filepath
        self.trace_function = trace_function
        self.trace_hash = None
        self.hash_correct = False

        if trace_filepath and trace_function and function_hash:
            self.trace_hash = self.__get_trace_hash_cpp(
                trace_filepath, trace_function).hexdigest()[0:9]

            if self.trace_hash == function_hash:
                self.hash_correct = True
            else:
                print("WARNING: Code hash does not match. Did you change the code? If yes, check that this requirements is still fullfilled by the function and update the hash.")
                print("  requirement:", text)
                print("  trace_file:", trace_filepath)
                print("  trace_function:", trace_function)
                print("  former  hash:", function_hash)
                print("  current hash:", self.trace_hash)
                exit(1)
        else:
            print("WARNING: Requirement is not traced yet.")
            print("  requirement:", text)

    def __get_trace_hash_cpp(self, trace_file: str, trace_function: str) -> str:
        file_path = Path(trace_file)
        function_block = cbse.cpp.get_function_body(file_path, trace_function)
        if not function_block:
            print("ERROR: Function block could not be retrieved.")
            return None
        return sha256.sha256(str.encode(function_block))

    def create_row(self):
        return [self.id, self.text, self.trace_filepath, self.trace_function, self.trace_hash, self.hash_correct]

    def create_header(self):
        return ["ID", "Text", "File Path", "Trace Function", "Current Hash", "Correct Hash"]