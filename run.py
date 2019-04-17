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

