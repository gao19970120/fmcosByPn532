import serial
from time import sleep


class Pn532(object):
    def __init__(self):
        pass

    def recv(self, serial):
        sleep(0.02)
        data = serial.read(100)
        # sleep(0.02)
        #
        # print(data)
        return data

    def nfcGetRecData(self):
        # sleep(0.5)
        recvdata = self.recv(nfc)
        len = bytes(bytearray(recvdata)[9:10])
        # print(len)
        return bytes(bytearray(recvdata)[11:11 + int.from_bytes(len, byteorder='big', signed=False)])

    def NfcReady(self):
        global nfc
        try:
            nfc = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
        except:
            nfc = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        nfc.write(
            b'\x55\x55\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x03\xFD\xD4\x14\x01\x17\x00')
        self.recv(nfc)

    def sendToNfc(self, data):
        len = 0
        dsum = 0
        for i in data:
            len = len + 1
            dsum = dsum + i
        lcs = 0xFF - len + 0x01
        dcs = 0xFF - dsum % 0x100 + 0x01
        redata = b'\x00\x00\xff' + bytes([len, lcs]) + bytes(data) + bytes([dcs, 0x00])
        # print(redata)
        nfc.write(redata)
        return redata

    def nfcFindCard(self):
        # sleep(0.1)
        self.sendToNfc([0xD4, 0x4A, 0x01, 0x00])
        recdata = self.recv(nfc)
        if recdata[11:13] == b'\xd5\x4b':
            global nfcing
            nfcing = 1
            uid = recdata[19:23]
            return uid
        else:
            return 'noCard'

    def nfcGetRecData(self):
        # sleep(0.1)
        recvdata = self.recv(nfc)
        # len = bytes(bytearray(recvdata)[9:10])
        len = recvdata[9]
        # return bytes(bytearray(recvdata)[11:11 + int.from_bytes(len, byteorder='big', signed=False)])
        return recvdata[11:11 + len]
