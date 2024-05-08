from time import sleep
import math

import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

class PressureSensor :
    # Gain = 1 : readings valtages between 0 to 4.096V
    GAIN = 1
    #ADS1115 precision : 16bits  
    ADC_RESOLUTION = 32767.0
    # V_REF : 3.3v
    VREF = 3.3

    def __init__(self) -> None:
        pass

    def pressureReadings(self) : 
        value = adc.read_adc(0, gain=GAIN)
        voltage = value / ADC_RESOLUTION * 4.096
        #Relation between psi and voltage is linear
        psi = 50.0 * voltage - 25.0
        #pression in Bar 
        bar = psi * 0.0689475729
        #pression in HPa and MPa
        MPa, HPa = bar * 0.1, bar * 1000
        return (psi, bar, MPa, HPa)