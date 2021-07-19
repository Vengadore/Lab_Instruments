""" Units are define by a "short" name and a long name.
    Each unit has its own representation and can mix with new units to create a new unit"""

class FUNDAMENTAL(object):
    """A fundamental unit representation has the following properties:
       - Value: float
       - Symbol: string
       - Name: string
       """
    def __init__(self,Value:float,Name:str,Symbol:str = None):
        # Set value to fundamental unit
        self.VALUE = Value
        self.NAME = Name.upper()
        if Symbol is None:
            self.SYMBOL = Name[0].upper()
        else:
            self.SYMBOL = Symbol
    def GET_VALUE(self):
        return self.VALUE

    def UNIT(self):
        return "{}".format(self.SYMBOL)

    def UNITName(self):
        return self.NAME

    def __str__(self):
        return "{}[{}]".format(self.GET_VALUE(), self.UNIT())

    def __repr__(self):
        return "{}[{}]".format(self.GET_VALUE(),self.UNIT())

    def __add__(self,other):
        if other.UNIT() == self.UNIT():
            return FUNDAMENTAL(self.GET_VALUE()+other.GET_VALUE(),self.UNITName(),self.UNIT())
    def __sub__(self, other):
        if other.UNIT() == self.UNIT():
            return FUNDAMENTAL(self.GET_VALUE() - other.GET_VALUE(), self.UNITName(), self.UNIT())

    def __mul__(self, other):
        return FUNDAMENTAL(self.GET_VALUE()*other.GET_VALUE(),
                           self.simplify_units(self.UNITName()+"."+other.UNITName()),
                           self.simplify_units(self.UNIT()+"."+other.UNIT()))

    def __truediv__(self, other):
        return FUNDAMENTAL(self.GET_VALUE()/other.GET_VALUE(),
                           self.simplify_units(self.UNITName()+"/"+other.UNITName()),
                           self.simplify_units(self.UNIT()+"/"+other.UNIT()))

    def simplify_units(self,units):
        if "/" not in units:
            return units
        UNITS = units.split('.')
        num = [i.split('/')[0] for i in UNITS]
        den = [i.split('/')[1] for i in UNITS if len(i.split('/'))>1]
        if len(num)>len(den):
            for i in den:
                if i in num:
                    num.remove(i)
                    den.remove(i)
        else:
            for i in num:
                if i in den:
                    den.remove(i)
                    num.remove(i)
        num = ".".join(num)
        if len(den) > 0:
            if len(den) == 1
            den = "/"+"/".join(den)
        else:
            return num
        return num+den





######################################################################
########################### BASIC UNITS ##############################
######################################################################

class VOLT(FUNDAMENTAL):
    """
    The representation of the VOLT given a fundamental structure
    """
    def __init__(self,Value:float):
        super().__init__(Value,"VOLT","V")

class AMPERE(FUNDAMENTAL):
    """
    The representation of the AMPERE given a fundamental structure
    """
    def __init__(self,Value:float):
        super().__init__(Value,"AMPERE","A")

class OHM(FUNDAMENTAL):
    """
    The representation of the OHM given a fundamental structure
    """
    def __init__(self,Value:float):
        super().__init__(Value, "OHM", "\u03A9")
    ## You can add ohm


class NULL(FUNDAMENTAL):
    """
    The representation of the NULL given a fundamental structure
    """
    def __init__(self,Value:float):
        super().__init__(Value, "NONE", "1")


######################################################################
######################### UNIT HANDLING ##############################
######################################################################





## TEST CODE ##
if __name__ == "__main__":
    V1 = VOLT(1)
    V2 = VOLT(4)
    O1 = OHM(10)
    print(V1/V1/O1)



