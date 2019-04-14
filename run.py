import fm1208




if __name__=='__main__':
    exam=fm1208.fmos()
    while(1):
        if input()=='findcard':
            print(exam.nfcFindCard())
        if input()=='selectcard':
            print(exam.nfcFindCard())
            print(exam.sendCommand(0x00,0xA4,0x00,0x00,0x02,[0x3f,0x00],0x00))