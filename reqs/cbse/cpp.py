import re

def get_function_body(file_path: str, function_signature: str) -> str:
    if not file_path.exists():
        print("ERROR: file_path does not exist:", file_path)
        return None

    with open(file_path.as_posix(), 'r') as reader:
        file_content = reader.read()
        # locate function
        function_signature_begin = file_content.find(function_signature)
        if function_signature_begin == -1:
            print("ERROR: could not find function_signature:\n  ", function_signature, "\n  in: ", file_path)
            return None
        # locate function block
        function_signature_end = function_signature_begin + len(function_signature)
        pattern = re.compile(r'(\{|\})')
        open_blocks = 0
        function_block_end = -1
        for curly_brace in pattern.finditer(file_content, pos=function_signature_end):
            symbol = curly_brace.group(0)
            if symbol == '{':
                open_blocks += 1
            elif symbol == '}':
                open_blocks -= 1
            if open_blocks == 0:
                function_block_end = curly_brace.span()[1]
                break
        if function_block_end == -1:
            print("ERROR: could not find function block end:\n  ", function_signature, "\n  in: ", file_path)
            return None
        # simplify whitespaces
        function_block = file_content[function_signature_begin:function_block_end]
        function_block = " ".join(function_block.split())
        return function_block