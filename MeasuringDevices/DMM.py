import pyvisa

class DMM_3458A:
    def __init__(self, address=0):
        rm = pyvisa.ResourceManager()
        ## Set
        self.instrument = rm.open_resource(rm.list_resources()[address], read_termination='\r')
        self.GPIB_Address = rm.list_resources()[address]
        self.IDN = self.instrument.query('ID?')
        print(self.IDN)
        self.instrument.timeout = 40000
        self.write("RESET")

    def write(self, data):
        self.instrument.write(data)

    def read(self):
        return self.instrument.read()

    def query(self, data):
        return self.instrument.query(data)

    def ACAL(self, function="ALL"):
        cal_values = ["ALL", "DCV", "AC", "OHMS"]
        if function in cal_values:
            try:
                self.write("ACAL " + function)
            except:
                temp = None
                while (temp != None):
                    try:
                        temp = self.get_temp()
                    except:
                        temp = None
            return 1
        else:
            return 0

    def get_temp(self):
        return self.query("TEMP?")

    def reset(self):
        self.write("RESET")

    def set_ACV(self, range=1):
        self.write("ACV " + str(range) + "0.00001")

    def set_ACVSYNC(self, range=1):
        self.write("ACV " + str(range) + ";")
        self.write("SETACV SYNC;")
        self.write("NPLC 100;NDIG 8;LFILTER ON;RES 0.000001")

    def set_DCV(self, range=1, NPLC=200):
        self.write("DCV " + str(range) + ";")
        self.set_NPLC(NPLC)

    def set_NPLC(self, NPLC=1):
        self.write("NPLC " + str(NPLC))

    def SAMPLE(self):
        self.write("TRIG SGL")
        return float(self.read())