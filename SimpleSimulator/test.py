s1 = '''
0x00010000:0b00000000000000000000000000001011
0x00010004:0b00000000000000000000000000000011
0x00010008:0b00000000000000000000000000000000
0x0001000c:0b00000000000000000000000000000000
0x00010010:0b00000000000000000000000000000000
0x00010014:0b00000000000000000000000000000000
0x00010018:0b00000000000000000000000000000000
0x0001001c:0b00000000000000000000000000000000
0x00010020:0b00000000000000000000000000000000
0x00010024:0b00000000000000000000000000000000
0x00010028:0b00000000000000000000000000000000
0x0001002c:0b00000000000000000000000000000000
0x00010030:0b00000000000000000000000000000000
0x00010034:0b00000000000000000000000000000000
0x00010038:0b00000000000000000000000000000000
0x0001003c:0b00000000000000000000000000000000
0x00010040:0b00000000000000000000000000000000
0x00010044:0b00000000000000000000000000000000
0x00010048:0b00000000000000000000000000000000
0x0001004c:0b00000000000000000000000000000000
0x00010050:0b00000000000000000000000000000000
0x00010054:0b00000000000000000000000000000000
0x00010058:0b00000000000000000000000000000000
0x0001005c:0b00000000000000000000000000000000
0x00010060:0b00000000000000000000000000000000
0x00010064:0b00000000000000000000000000000000
0x00010068:0b00000000000000000000000000000000
0x0001006c:0b00000000000000000000000000000000
0x00010070:0b00000000000000000000000000000000
0x00010074:0b00000000000000000000000000000000
0x00010078:0b00000000000000000000000000000000
0x0001007c:0b00000000000000000000000000000000
'''
s2 = '''
0x00010000:00000000000000000000000000001011
0x00010004:00000000000000000000000000000011
0x00010008:00000000000000000000000000000000
0x0001000c:00000000000000000000000000000000
0x00010010:00000000000000000000000000000000
0x00010014:00000000000000000000000000000000
0x00010018:00000000000000000000000000000000
0x0001001c:00000000000000000000000000000000
0x00010020:00000000000000000000000000000000
0x00010024:00000000000000000000000000000000
0x00010028:00000000000000000000000000000000
0x0001002c:00000000000000000000000000000000
0x00010030:00000000000000000000000000000000
0x00010034:00000000000000000000000000000000
0x00010038:00000000000000000000000000000000
0x0001003c:00000000000000000000000000000000
0x00010040:00000000000000000000000000000000
0x00010044:00000000000000000000000000000000
0x00010048:00000000000000000000000000000000
0x0001004c:00000000000000000000000000000000
0x00010050:00000000000000000000000000000000
0x00010054:00000000000000000000000000000000
0x00010058:00000000000000000000000000000000
0x0001005c:00000000000000000000000000000000
0x00010060:00000000000000000000000000000000
0x00010064:00000000000000000000000000000000
0x00010068:00000000000000000000000000000000
0x0001006c:00000000000000000000000000000000
0x00010070:00000000000000000000000000000000
0x00010074:00000000000000000000000000000000
0x00010078:00000000000000000000000000000000
0x0001007c:00000000000000000000000000000000
'''

if s1 == s2:
    print("yay")
