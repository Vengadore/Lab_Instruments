import xml.etree.ElementTree as ET

class Instrument:
    def __init__(self,path:str):
        self.ORIGIN = path
        self.ROOT = ET.parse(self.ORIGIN)
        print(self.ROOT.find('INFORMATION').find("MFR").text)



if __name__ == "__main__":
    I = Instrument("Example.xml")
