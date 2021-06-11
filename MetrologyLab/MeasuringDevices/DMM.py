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
    
class DMM_34401A:
    def __init__(self,address = 0):
        self.inst = rm.open_resource(pv.ResourceManager().list_resources()[address])
        self.inst.timeout = 250000
        self.inst.write('*RST')
        print(self.inst.query('*IDN?'))
    def write(self,string):
        self.inst.write(string)
    def read(self):
        self.inst.read()
    def query(self,string):
        return self.inst.query(string)
    def AC_config(self,R = 1,Res = 0.00001):
        self.write('CONF:VOLT:AC {}, {}'.format(R,Res))
        self.write('SAMPle:COUNt 10')
        self.write('CALCulate:FUNCtion AVERage')
        self.write('CALCulate:STATe ON')
        self.write('DET:BAND 3')
    def Get_funciton(self):
        return self.query('FUNCtion?')
    def Trigger(self):
        self.write('CALCulate:STATe OFF')
        self.write('CALCulate:STATe ON')
        self.write('INITiate')
    def Measure_AC(self):
        self.Trigger()
        self.query('*OPC?')
        R = self.query('READ?').split(',')
        R = [float(f) for f in R[0:-1]] + [float(R[-1].split('\\')[0])] 
        return R
