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
            
