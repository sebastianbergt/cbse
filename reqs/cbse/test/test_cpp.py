import pytest
import cbse.cpp
from pathlib import Path

def test_get_function_body():
    file_path = Path(__file__).parent / 'src' / 'test.cpp'
    function_signature = 'bool isValueEven()'
    function_body = cbse.cpp.get_function_body(file_path, function_signature)
    assert function_body == "bool isValueEven() { if (value_ % 2 == 0) { return true; } else { return false; } }"

