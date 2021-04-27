UNITS = {"V":"VOLT",
         "A":"AMPERE",
         "OHM":"OHM",
         "°C":"DEGREE CELSIUS",
         "°F":"DEGREE FAHRENHEIT",
         "°K":"DEGREE KELVIN",
         "C":"COULOMB"}


class SPECIFICATION:
    """
    Specification refers to the value of how much the instrument can differ from its true measurand.
    It tends to change in function of the time from the last calibration, and sometimes it tends to change
    due to special functions.
    """
    def __init__(self,specs:dict,floor:dict,Range:float):
        """
        Define a specification using ppm, use a dictionary to specify the ppm value,
        :param specs: {'ppm':0.0,'percentage':0.0}
        :param floor: {'ppm':0.0,'percentage':0.0}
        """
        self.specs = specs
        self.floor = floor
        self.Range = Range

        if "ppm" in self.specs.keys():
            # compute percentage
            self.specs['%'] = self.specs['ppm']*0.0001
            self.floor['%'] = self.floor['ppm']*0.0001
        elif "%" in self.specs.keys():
            self.specs['ppm'] = self.specs['%']*10000
            self.floor['ppm'] = self.floor['%']*10000

    def LIMITS(self,VALUE:float):
        """
        :param VALUE: Value to use to compute uncertanty
        :return: Upper and lower possible values
        """
        x = self.specs['%']/100*VALUE+self.floor['%']*self.Range
        return (VALUE-x,VALUE+x)

    def ACCURACY(self,VALUE:float):
        x = self.specs['%'] * VALUE / 100 + self.floor['%'] * self.Range / 100
        return x


class DEVICE_RANGE:
    """
    This class represents a range of any instrument, intruments tend to follow the same characteristics:
    - Range
    - Unit
    - Full_scale
    - Specification
    - 10% of the range

    As an example. Let's talk about the
    """

    def __init__(self, Range:float, Unit:str, Specification: SPECIFICATION, Full_scale:float = None):
        """
        Define a range for an instrument, for more information read the datasheet of the instrument.

        :param Range: Range of the instrument [1,10,100]
        :param Unit:  Units of the range [Volts,Ampere,Ohms]
        :param Specification: Accuracy specification of a range according to a range (see datasheet)
        :param Full_scale: Max value for the range
        """

        self.RANGE = Range
        self.UNIT = Unit
        self.SPEC = Specification

        if Full_scale == None:
            self.Full_scale = Range
        else:
            self.Full_scale = Full_scale

    def OUTPUT(self, X:float):
        return (X, self.SPEC.LIMITS(X))

    __call__ = OUTPUT

