import time
import math
from datetime import datetime

import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

class PressureSensor :
    # Gain = 1 : readings valtages between 0 to 4.096V
    GAIN = 1
    #ADS1115 precision : 16bits  
    ADC_RESOLUTION = 32767.0
    # V_REF : 3.3v
    VREF = 3.3

    def __init__(self, gain=GAIN, resolution=ADC_RESOLUTION, vref=VREF) :
        self.GAIN = gain
        self.ADC_RESOLUTION = resolution
        self.VREF = vref
        self.psi = 0
        self.bar = 0
        self.HPa = 0
        self.MPa = 0

    def pressureReadings(self) : 
        value = adc.read_adc(0, gain=GAIN)
        voltage = value / ADC_RESOLUTION * 4.096
        #Relation between psi and voltage is linear
        self.psi = 50.0 * voltage - 25.0
        #pression in Bar 
        self.bar = self.psi * 0.0689475729
        #pression in HPa and MPa
        self.MPa, self.HPa = self.bar * 0.1, self.bar * 1000
        #return (self.psi, self.bar, self.MPa, self.HPa)
    
    def getPressureInBar(self) :
        return  self.bar
    
    def getPressureInHPa(self) :
        return self.HPa
    
    def getPressureInMPa(self) :
        return self.MPa
  
def main() :
    gain = 1
    adcResolution = 32767.0
    vref = 3.3

    pressure = PressureSensor(gain, adcResolution, vref) 

    while True :
        timestamp = str(datetime.now())
        pressure.pressureReadings()
        print("Psi = {}".format(psi))
        print("Pression (bar) = {} Bar".format(pressure.getPressureInBar()))
        print("Pression (MPa) = {} Bar".format(pressure.getPressureInMPa()))
        print("Pression (HPa) = {} Bar".format(pressure.getPressureInHPa()))

        time.sleep(10)

if __name__ == '__main__':
   main()



