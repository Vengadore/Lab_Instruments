""" Units are define by a "short" name and a long name.
    Each unit has its own representation and can mix with new units to create a new unit"""

class VOLT:
    def __init__(self,Value:float):
        self.value = Value
    def get_value(self):
        return self.value
    def __repr__(self):
        return str(self.value) + "[V]"
    def get_unit(self):
        return "[V]"
    def get_lunit(self):
        return "VOLT"
    def __str__(self):
        return str(self.get_value())+self.get_unit()

    def __add__(self, other):
        if other.get_unit() == self.get_unit():
            return VOLT(self.get_value()+other.get_value())

    def __truediv__(self, other):
        if other.get_unit() == self.get_unit():
            return self.get_value()/other.get_value()
        elif other.get_lunit() == "OHM":
            return AMPERE(self.get_value()/other.get_value())
        elif other.get_lunit() == "AMPERE":
            return OHM(self.get_value()/other.get_value())


class AMPERE:
    def __init__(self,Value:float):
        self.value = Value
    def get_value(self):
        return self.value
    def __repr__(self):
        return str(self.value) + "[A]"
    def get_unit(self):
        return "[A]"
    def get_lunit(self):
        return "AMPERE"
    def __str__(self):
        return str(self.get_value())+self.get_unit()

    def __add__(self, other):
        if other.get_unit() == self.get_unit():
            return AMPERE(self.get_value()+other.get_value())



class OHM:
    def __init__(self,Value:float):
        self.value = Value
    def get_value(self):
        return self.value
    def __repr__(self):
        return str(self.value) + "[\u03A9]"
    def get_unit(self):
        return "[\u03A9]"
    def get_lunit(self):
        return "OHM"
    def __str__(self):
        return str(self.get_value())+self.get_unit()

    def __add__(self, other):
        if other.get_unit() == self.get_unit():
            return OHM(self.get_value()+other.get_value())

    def __mul__(self, other):
        #if other.get_unit() == self.get_unit():
        #    return self.get_value()/other.get_value()
        if other.get_lunit() == "AMPERE":
            return VOLT(self.get_value()*other.get_value())
