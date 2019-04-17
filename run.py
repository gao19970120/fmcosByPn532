import fm1208

if __name__ == '__main__':
    exam = fm1208.fmcos()
    while (1):
        inp=input()
        if inp == 'findcard':
            print(exam.nfcFindCard())
        if inp == 'selectcard':
            print(exam.nfcFindCard())
            print(exam.fmcosSelect('3f00'))
            ram=exam.sendCommand(0x00,0x84,0x00,0x00,le=0x08)
            print(ram)
            key=b'\xff\xff\xff\xff\xff\xff\xff\xff'
            DESECB=fm1208.DES.new(key,fm1208.DES.MODE_ECB)
            DESED=DESECB.encrypt(ram)
            print(exam.sendCommand(0x00,0x82,0x00,0x00,Data=DESED))
            print(exam.sendCommand(0x80,0xE0,0x00,0x3f,Data=b'\x38\xff\xff\x1f\x22\x81\xff\xfftlulock'))

