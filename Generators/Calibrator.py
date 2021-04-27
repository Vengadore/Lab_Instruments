import pyvisa

class CAL_5500A:
    def __init__(self, address=0):
        rm = pyvisa.ResourceManager()
        ## Set
        self.instrument = rm.open_resource(rm.list_resources()[address], read_termination='\n')
        self.GPIB_Address = rm.list_resources()[address]
        self.IDN = self.instrument.query('*IDN?')
        print(self.IDN)
        self.instrument.timeout = 40000
        self.write("RESET")

    def write(self, data):
        self.instrument.write(data)

    def read(self):
        return self.instrument.read()

    def query(self, data):
        return self.instrument.query(data)

    def WAIT(self):
        self.write(";*WAI")

    def SET_Output(self, amplitude, unit="V", frequency=0):
        self.write("OUT " + str(amplitude) + " " + str(unit))
        self.WAIT()
        self.write("OUT " + str(frequency) + " HZ")
        self.WAIT()

    def OPERATE(self):
        self.WAIT()
        self.write("OPER")

    def STBY(self):
        self.WAIT()
        self.write("STBY")