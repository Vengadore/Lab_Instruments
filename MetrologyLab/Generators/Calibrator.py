import pyvisa
import metrolopy as uc

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

class MFC:
    """MFC: Multi Function Calibrator
    This class describes the body of a common multi-function calibrator by FLUKE.
    These calibrators are capable of working with magnitudes such as:
    - Voltage DC
    - Voltage AC
    - Current DC
    - Current AC
    - Resistance
    - Thermocouples
    - Capacitance
    """
    def __init__(self,MODEL:str):
        self.MODEL = MODEL
        self.MFR = "FLUKE"

    class mode:
        """mode defines a capability of the instrument"""
        def __init__(self,unit:uc.unit, max:float,min:float = 0,correction:lambda = lambda x = 0):
            self.unit = unit
            self.MAX = max
            self.MIN = min
            self.error = correction
            self.uncertanty =
        def f(self,x):
            return x + self.error(x)


