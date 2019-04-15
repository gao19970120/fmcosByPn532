import fm1208

if __name__ == '__main__':
    exam = fm1208.fmos()
    while (1):
        inp=input()
        if inp == 'findcard':
            print(exam.nfcFindCard())
        if inp == 'selectcard':
            print(exam.nfcFindCard())
            print(exam.fmosSelect('3f00'))

