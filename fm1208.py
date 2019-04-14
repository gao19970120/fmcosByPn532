import pn532


class fmos(pn532.Pn532):
    def __init__(self):
        self.NfcReady()
        pass

    def sendCommand(self, cla, ins, p1, p2, lc=None, Data=None, le=None):
        context = [0xD4, 0x40, 0x01, cla, ins, p1, p2]
        if lc != None:
            if len(Data) == lc:
                context = context + [lc] + list(Data)
            else:
                print(lc)
                print(len(Data))
                print('error len')
        if le != None:
            context = context + [le]
        if lc == None and le == None:
            context = context + [0x00]
        print(bytes(context))
        pn532.nfc.write(self.sendToNfc(context))
        recdata = self.fmosGetRecData(le)

        return recdata

    def fmosGetRecData(self,le):
        nfcdata = self.nfcGetRecData()
        if nfcdata[0:2]==b'\xd5\x41':
            if nfcdata[len(nfcdata) - 2:len(nfcdata)] == b'\x90\x00':
                if len(nfcdata)==le+4 or le == 0:

                    if le!=0:
                        return nfcdata[2:2+le]
                    else:
                        return nfcdata[2:len(nfcdata)-2]
                else:
                    return 'error'
            else:
                return 'error'
