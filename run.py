import fm1208

if __name__ == '__main__':
    exam = fm1208.fmcos()
    while (1):
        inp=input()
        if inp == 'duka':
            print(exam.nfcFindCard())
            print(exam.fmcosSelect('3f00'))
        if inp == 'faka':
            print(exam.nfcFindCard())
            print(exam.fmcosSelect('3f00'))
            #print(exam.sendCommand(0x80,0xe0,0x00,0x00,Data=b'\x3f\x00\x40\x01\xf0\xff\xff'))
            #print(exam.sendCommand(0x80,0xd4,0x39,0x01,Data=b'\x39\xf0\xf0\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff'))
            print(exam.fmcosSelect('3f00'))
            ram=exam.sendCommand(0x00,0x84,0x00,0x00,le=0x04)
            ram=ram+b'\x00\x00\x00\x00'
            print(ram)
            key=b'\xff\xff\xff\xff\xff\xff\xff\xff'
            DESECB=fm1208.DES.new(key,fm1208.DES.MODE_ECB)
            DESED=DESECB.encrypt(ram)
            print(exam.sendCommand(0x00,0x82,0x00,0x01,Data=DESED))
            #print(exam.sendCommand(0x80, 0xE0, 0x00, 0x3f, Data=b'\x38\xff\xff\xf0\x22\x81\xff\xfftlulock'))


