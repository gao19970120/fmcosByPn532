import pn532


class fmos(pn532.Pn532):
    def __init__(self):
        self.NfcReady()
        pass
