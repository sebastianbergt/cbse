from cbse.doc import Doc, Req, ReqType, Path

d = Doc(__file__)

d.req(1, "Check for even value.", ReqType.BASIC, \
    Path('src') / 'module1.cpp', 'bool isValueEven()', '206222c5b' )

d.req(2, "Something shall be done.", ReqType.BASIC)

d.export( Path('out') / 'module1_requirements.py.pdf')