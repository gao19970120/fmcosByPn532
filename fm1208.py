import pn532


def TLVanalysis(TLV):
    sum = 0
    TLVdict = {}
    while (1):
        try:
            tag = TLV[sum]
            length = TLV[sum + 1]
            value = TLV[sum + 2:sum + 2 + length]
            TLVdata = {'tag': tag, 'length': length, 'value': value}
            TLVdict[tag] = value
            sum = sum + length + 2
            if sum >= len(TLV):
                break
        except:
            return 'error'
    return TLVdict


def strToint16(str):
    int16 = []
    sum = 0
    for i16 in str:
        if sum % 2 != 0:
            int16 = int16 + [int(str[sum - 1:sum + 1], base=16)]
        sum = sum + 1
    return int16


class fmos(pn532.Pn532):
    def __init__(self):
        self.NfcReady()
        pass

    def sendCommand(self, cla, ins, p1, p2, Data=None, le=None):
        context = [0xD4, 0x40, 0x01, cla, ins, p1, p2]
        if Data != None:
            lc = len(Data)
        else:
            lc = None
        if lc != None:
            context = context + [lc] + list(Data)

        if le != None:
            context = context + [le]
        if lc == None and le == None:
            context = context + [0x00]
        print(bytes(context))
        self.sendToNfc(context)
        recdata = self.fmosGetRecData(le)

        return recdata

    def fmosGetRecData(self, le):
        nfcdata = self.nfcGetRecData()
        if nfcdata != 'error':
            if nfcdata[0:3] == b'\xd5\x41\x00':
                if nfcdata[-2:] == b'\x90\x00':
                    if le != None:
                        if (len(nfcdata) == le + 4) or le == 0:

                            if le != 0:
                                data = nfcdata[3:3 + le]
                            else:
                                # print(nfcdata[2:len(nfcdata) - 2])
                                return nfcdata[3:- 2]
                        else:
                            return 'error'
                else:
                    return nfcdata[-2:]
    def fmosReadRecord(self, ):
    def fmosSelect(self, fileID):
        fileIDlist = strToint16(fileID)
        answer = self.sendCommand(0x00, 0xA4, 0x00, 0x00, fileIDlist, 0x00)
        if answer != 'error':
            TLVdict = TLVanalysis(answer)
            TLVdict1 = TLVanalysis(TLVdict[0x6f])
            DFName = TLVdict1[0x84]
            ctrlMsg = TLVdict1[0xA5]
            return DFName
        else:
            return 'error'
