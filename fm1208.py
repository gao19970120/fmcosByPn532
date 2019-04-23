import pn532
from Crypto.Cipher import DES
import os


def TLVanalysis(TLV, tagLen=1):
    sum = 0
    TLVdict = {}
    while (1):
        try:
            tag = TLV[sum:sum + tagLen]
            try:
                length = TLV[sum + tagLen]
            except:
                TLVdict[tag] = b'None'
                break
            value = TLV[sum + tagLen + 1:sum + tagLen + 1 + length]
            TLVdata = {'tag': tag, 'length': length, 'value': value}
            TLVdict[tag] = value
            sum = sum + length + tagLen + 1
            if sum >= len(TLV):
                break
        except:
            return 'error'
    return TLVdict


def TLVcreate(tag, value):
    len = len(value)
    TLVdata = tag + bytes([len]) + value
    return TLVdata


def strToint16(str):
    int16 = []
    sum = 0
    for i16 in str:
        if sum % 2 != 0:
            int16 = int16 + [int(str[sum - 1:sum + 1], base=16)]
        sum = sum + 1
    return int16


class fmcos(pn532.Pn532):
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
        recdata = self.fmcosGetRecData(le)

        return recdata

    def fmcosGetRecData(self, le):
        nfcdata = self.nfcGetRecData()
        print(nfcdata)
        if nfcdata != 'error':
            if nfcdata[0:3] == b'\xd5\x41\x00':
                if nfcdata[-2:] == b'\x90\x00':
                    if len(nfcdata) != 5:
                        if le == None:
                            le = 0
                        if (len(nfcdata) == le + 5) or le == 0:

                            if le != 0:
                                return nfcdata[3:3 + le]
                            else:
                                # print(nfcdata[2:len(nfcdata) - 2])
                                return nfcdata[3:- 2]
                        else:
                            return 'error len'
                    else:
                        return 'success'
                else:
                    return nfcdata[-2:]

    # def fmcosReadRecord(self, ):
    def fmcosSelect(self, fileID):
        fileIDlist = strToint16(fileID)
        answer = self.sendCommand(0x00, 0xA4, 0x00, 0x00, fileIDlist, 0x00)
        if answer != 'error':
            try:
                TLVdict = TLVanalysis(answer)
                TLVdict1 = TLVanalysis(TLVdict[b'\x6f'])
                DFName = TLVdict1[b'\x84']
                try:
                    ctrlMsg = TLVdict1[b'\xa5']
                    try:
                        ctrlMsg = TLVanalysis(ctrlMsg)[b'\x88']
                    except:
                        try:
                            ctrlMsg = TLVanalysis(ctrlMsg, tagLen=2)[b'\x9f\x0c']
                        except:
                            ctrlMsg = b'noCtrlMsg'

                except:
                    ctrlMsg = b'noCtrlMsg'

                print(ctrlMsg)
                return DFName
            except:
                return answer
        else:
            return 'error'
