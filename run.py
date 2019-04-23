import fm1208

if __name__ == '__main__':
    exam = fm1208.fmcos()
    while (1):
        inp = input()
        if inp == 'duka':
            while (exam.nfcFindCard() == 'noCard'):
                print('noCard')
            try:
                #print(exam.fmcosSelect('3f00'))
                ram = exam.sendCommand(0x00, 0x84, 0x00, 0x00, le=0x04)
                ram = ram + b'\x00\x00\x00\x00'
                print(ram)
                key = b'\xff\xff\xff\xff\xff\xff\xff\xff'
                DESECB = fm1208.DES.new(key, fm1208.DES.MODE_ECB)
                DESED = DESECB.encrypt(ram)
                print(exam.sendCommand(0x00, 0x82, 0x00, 0x03, Data=DESED))
                print(exam.fmcosSelect('3f01'))
                ram=fm1208.os.urandom(8)
                DESED=exam.sendCommand(0x00,0x88,0x00,0x01,Data=ram)
                print(DESED)
                key = b'\xff\xff\xff\xff\xff\xff\xff\xff'
                DESECB = fm1208.DES.new(key, fm1208.DES.MODE_ECB)
                if DESED==DESECB.encrypt(ram):
                    print('INTERNAL AUTHENTICATE success')
            except:
                pass
        if inp == 'faka':
            while (exam.nfcFindCard() == 'noCard'):
                print('noCard')
            try:
                print(exam.fmcosSelect('3f00'))

                print(exam.sendCommand(0x80, 0xe0, 0x00, 0x00, Data=b'\x3f\x00\xf0\x01\xf4\xff\xff'))
                print(exam.sendCommand(0x80, 0xd4, 0x01, 0x01,
                                       Data=b'\x39\xf0\xf4\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff'))
                print(exam.sendCommand(0x80, 0xd4, 0x01, 0x02,
                                       Data=b'\x39\xf0\xf4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff'))
                print(exam.sendCommand(0x80, 0xd4, 0x01, 0x03,
                                       Data=b'\x39\xf0\xf3\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff'))

                print(exam.sendCommand(0x80, 0xE0, 0x3f, 0x01, Data=b'\x38\x0f\xff\xf4\xf4\x81\xff\xfftlulock'))
                print(exam.fmcosSelect('3f01'))
                print(exam.sendCommand(0x80, 0xe0, 0x00, 0x00, Data=b'\x3f\x00\xf0\x81\xf4\xff\xff'))
                print(exam.sendCommand(0x80, 0xd4, 0x01, 0x01,
                                       Data=b'\x34\xf3\xf4\x05\x98\xff\xff\xff\xff\xff\xff\xff\xff'))
                print(exam.sendCommand(0x80, 0xE0, 0x00, 0x01, Data=b'\x28\x00\xff\xf0\xf4\xff\xf1'))
                print(exam.fmcosSelect('0001'))
                print(exam.sendCommand(0x00, 0xd6, 0x00, 0x00, Data=b'appForTlulock'))

            except:
                pass

        if inp == 'clear':
            while (exam.nfcFindCard() == 'noCard'):
                print('noCard')
            try:
                print(exam.fmcosSelect('3f00'))
                ram = exam.sendCommand(0x00, 0x84, 0x00, 0x00, le=0x04)
                ram = ram + b'\x00\x00\x00\x00'
                print(ram)
                key = b'\xff\xff\xff\xff\xff\xff\xff\xff'
                DESECB = fm1208.DES.new(key, fm1208.DES.MODE_ECB)
                DESED = DESECB.encrypt(ram)
                print(exam.sendCommand(0x00, 0x82, 0x00, 0x01, Data=DESED))
                print(exam.sendCommand(0x80, 0x0e, 0x00, 0x00))
            except:
                pass
