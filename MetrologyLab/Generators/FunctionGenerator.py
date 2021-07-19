import pyvisa

class Siglent_SDG2122X:
    def __init__(self,address = 0):
        self.inst = pyvisa.ResourceManager().open_resource(pyvisa.ResourceManager().list_resources()[address])
        self.inst.timeout = 25000
        self.inst.write('*RST')
        print(self.inst.query('*IDN?'))
    def write(self,string):
        self.inst.write(string)
    def read(self):
        self.inst.read()
    def query(self,string):
        return self.inst.query(string)
    def set_channel_state(self,channel=1,state = False):
        self.write('C{}:OUTP {}'.format(channel,"ON" if state else "OFF"))
    def set_channel_impedance(self,channel = 1, impedance = 50):
        self.write('C{}:OUTP LOAD,{}'.format(channel,50 if type(impedance) == int else "HZ"))
    def ouput_waveform(self,channel,A = 1,F = 60):
        self.write('C{}:BSWV SINE,AMP,{},FRQ,{}'.format(channel,A,F))

class PWRSupply:
    """Class created for Agilent 66xxA Power Supply"""
    def __init__(self,address:int=0):
        self.inst = pyvisa.ResourceManager().open_resource(pyvisa.ResourceManager().list_resources()[address])
        self.SETUP(TimeOut=25000)

    # Normal control functions
    def __IDN__(self):
        """This query requests the device to identify itself.
        It returns a string composed of four fields separated by commas."""
        return self.query("*IDN?")
    def CLS(self):
        """Clear Status"""
        self.write("*CLS")
        return True
    def OPC(self):
        """This query waits until all the previous operations are completed"""
        self.query("*OPC?")
        return True
    def RST(self):
        """ This command resets the device to a factory-defined state. """
        self.write("*RST")
        self.OPC()
        return True
    def WAIT(self):
        """ This command instructs the device not to process futher operations unitl pending operations are completed. """
        self.write("*WAI")
        return True
    def SETUP(self,TimeOut:int = 25000):
        """ This command configures the device"""
        # Timeout configuration
        self.inst.timeout = TimeOut
        self.CLS()
        self.RST()
        self.WAIT()
        # Presentation of the device
        print(self.__IDN__())
        return True

    # General sending and reveiving commands
    def write(self, string):
        """This function writes a command into the BUS line"""
        self.inst.write(string)
    def read(self):
        """This function **reads** the values from the BUS line"""
        self.inst.read()
    def query(self, string):
        """ This functions sends a command and watis for a response"""
        return self.inst.query(string)

    # Instrument commands
    def SET_OUTPUT_VOLTAGE(self,VOLTAGE:float = 1):
        """This command sets the output voltage of the power supply"""
        self.write("VOLT {}".format(VOLTAGE))
        self.WAIT()
        return "Programmed Voltage level {} [V]".format(self.query("VOLT?"))
    def SET_OUTPUT_CURRENT(self,CURRENT:float = 1):
        """This command sets the output voltage of the power supply"""
        self.write("CURR {}".format(CURRENT))
        self.WAIT()
        return "Programmed Current level {} [A]".format(self.query("CURR?"))
    def SET_CHANNEL_STATE(self,STATE:bool = False):
        """ This command toggles the output state between ON and OFF"""
        if STATE:
            self.write("OUTP ON")
        else:
            self.write("OUTP OFF")
        self.WAIT()
        return True
    def SET_MAX_CURRENT(self,MAX_CURRENT):
        """ This command sets the maximum current to provide to the circuit"""
        # Set max level
        self.write("CURR:LEV {};PROT:STAT ON".format(MAX_CURRENT))
        self.WAIT()
        # Read stored level
        return "The current level has been set to {}".format(self.query("CURR:LEV?;PROT;STAT?"))
    def SET_MAX_VOLTAGE(self,MAX_VOLTAGE,PROTECTION = 1.2):
        """ This command sets the maximum current to provide to the circuit"""
        # Set max level
        self.write("VOLT:LEV {};PROT {}".format(MAX_VOLTAGE,MAX_VOLTAGE*PROTECTION))
        self.WAIT()
        # Read stored level
        return "The voltage level has been set to {}".format(self.query("VOLT:LEV?;PROT?;"))
    def SET_CC_MODE(self):
        """ This coomand sets the Power Supply into CONSTANT CURRENT mode"""
        self.write("STAT:OPER:ENAB 1024;PTR 1024")
        self.WAIT()
        return True
    def SET_CV_MODE(self):
        """ This coomand sets the Power Supply into CONSTANT VOLTAGE mode"""
        self.write("STAT:OPER:ENAB 256;PTR 256")
        self.WAIT()
        return True

