import metrolopy as uc
import functools


class Fluke_5522A:
    def __init__(self):
        self.MODEL = "5522A"
        self.MFR = "FLUKE"
        ## Fluke Generators
        self.V_DC = InstFunciton(unit = uc.unit('V'),ranges = [
            Interval(limits=[0, 329.9999E-3],
                     nominal=lambda x : uc.gummy(x,unit = "mV",u = 20, uunit = "ppm"),
                     error=lambda x: uc.gummy(0,unit = "mV",u = 0,uunit = "ppm"),
                     resolution=0.0001,
                     u_floor=uc.gummy(x=0, u=1, unit="mV", uunit="uV"),
                     u_foor_stability=uc.gummy(x=0, u=1, unit="mV", uunit="uV"),
                     u_resolution=uc.gummy(uc.UniformDist(center=0, half_width=0.0001 / 2), unit="mV", uunit="mV")),
            Interval(limits=[0, 3.2999999E0],
                     nominal=lambda x: uc.gummy(x, unit="V", u=11, uunit="ppm"),
                     error=lambda x :uc.gummy(0, unit="V", u=0, uunit="ppm"),
                     resolution=0.000001,
                     u_floor=uc.gummy(x=0, u=1, unit="V", uunit="uV"),
                     u_foor_stability=uc.gummy(x=0, u=1, unit="V", uunit="uV"),
                     u_resolution=uc.gummy(uc.UniformDist(center=0, half_width=0.0001 / 2), unit="mV", uunit="mV"))
        ])


        ## DEFINITION OF INTERVALS


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
    the calibration certificate will give you the correct value that sometimes can be fitted into a curved
    and is always associated to an uncertainty.
    Instrument intervals tend to have a minimum and maximum value of operation.
    A function can map the nominal value to a real value with a certain uncertainty.

    """

    def function(self, x=None):
        return x

    def __init__(self,limits:list = [],
                 nominal:function = lambda x:uc.gummy(x),
                 error:function = lambda x:0,
                 resolution = 0.1E-16,
                 **kwargs):
        self.NOMINAL = nominal
        self.E = error
        self.min = min(limits)
        self.max = max(limits)
        self.unit = self.NOMINAL(0).unit
        self.Res = resolution
        self.u = []
        ## Uncertainties from different sources
        for key in kwargs:
            if "u_" in key:
                self.u.append(kwargs[key])

    def __call__(self,x):
        """Compute the uncertainty for a given value"""
        return functools.reduce(lambda a,b:a+b,[self.NOMINAL(x),-self.E(x)]+self.u)


if __name__ == "__main__":
    I = Fluke_5522A()