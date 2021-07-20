import xml.etree.ElementTree as ET
import metrolopy as uc


class Instrument:
    def __init__(self, path: str):
        self.ORIGIN = path
        self.ROOT = ET.parse(self.ORIGIN)
        print(self.ROOT.find('INFORMATION').find("MFR").text)


class InstFunciton:
    """An instrument function describes the capability of any instrument.
    It describes the capability to measure or generate a certain value or quantity.
    Inside of it certain ranges can be found."""

    def __init__(self, unit: uc.unit('V'), ranges: list, mode: str = "G"):
        """
        :param unit: object
        :param ranges: list
        :param mode: Generate/Measure
        """
        self.unit = unit
        self.RANGES = ranges
        self.MODE = "Generator" if mode == "G" else "Meter"



class Interval:
    """ An Interval is the fundamental configuration of any equipment.
    An equipment has always a nominal value that can be corrected given a calibration certificate,
    they tend to have a minimum and maximum value of operation. A function can map the nominal value
    to a real value with a certain uncertainty."""

    def function(self):
        return x

    def __init__(self,max,min = 0,nominal:function = lambda x:uc.gummy(x),error:function = lambda x:0,**kwargs):
        self.NOMINAL = nominal
        self.E = error
        self.min = min
        self.max = max
        self.unit = self.NOMINAL(self.min).unit


        ## Uncertainties from different sources



    def __call__(self,x):
        return self.NOMINAL(x)-self.E(x)




if __name__ == "__main__":
    I = Interval(max = 0.3299999,
                 min = 0,
                 nominal= lambda x:(uc.gummy(x,unit = 'mV',u = 15,uunit='ppm')),
                 error = lambda x:uc.gummy(0.0,unit = 'mV',u= 0,uunit='ppm'))
    I.style = "+-"

    print(I(100))


