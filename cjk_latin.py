import unicodedata

START = 0x00
END = 0x110000

OUT_FILE = open("charindex-utf8-unilatin.txt", "w", encoding="utf8")
TITLE = """UNICODE TABLE - LATIN
RANGE: 
+==============+==============+===========+=============================================================+=============+===================+========================+
|ORDINAL(DEC)  |ORDINAL(HEX)  |CHARACTER  |CHARACTER NAME                                               |ISPRINTABLE  |CHARACTER_IN_HTML  |CHARACTER_BYTES         |
"""
OUT_FILE.write(TITLE)
LENGTH_ORDINAL_DEC = 12
LENGTH_ORDINAL_HEX = 12
LENGTH_CHR_NAME = 68
LENGTH_PRINTABLE = 11
LENGTH_HTML = 17
LENGTH_CHR = 9

def list_to_hex(l:list[int]):
    for obj in l:
        yield hex(obj)[2:].zfill(2)

def getname(c):
    try:
        return unicodedata.name(c)
    except ValueError:
        return "<NOT A CHARACTER>"

for ordinal in range(START, END):
    char = chr(ordinal)
    name = getname(char)
    if not name.startswith("LATIN"):
        continue
    try:
        B_LIST = list(list_to_hex(list(char.encode(errors="surrogateescape"))))
    except UnicodeEncodeError as err:
        B_LIST = err.reason
    ORD_DEC = str(ordinal)
    ORD_HEX = hex(ordinal)[2:]
    printable = char.isprintable()
    html_name = "&#%s;"% ORD_DEC
    c_str = char if printable else "UNKDOWN"
    print("Processing %s......"% ordinal)
    s = "|%12s  |%12s  |%s  |%s  |%11s  |%17s  |%24s|\n"% (ORD_DEC, ORD_HEX, c_str.rjust(9), name.ljust(59), printable, html_name, " ".join(B_LIST).ljust(24))
    OUT_FILE.write(s)
    
OUT_FILE.write("+==============+==============+=========+=============================================================+=============+===================+========================+")
OUT_FILE.close()