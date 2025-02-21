import RPi.GPIO as GPIO
import time

class RelayCommand :
    
    def __init__(self, pin) :
        self.RELAYPIN = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)         
        GPIO.setup(self.RELAYPIN, GPIO.OUT)
    
    def onRelay(self):
        try:
            GPIO.output(self.RELAYPIN, GPIO.HIGH)
            #state = GPIO.input(self.RELAYPIN)
        except KeyboardInterrupt:  # Interruption avec 'Ctrl+C'
            GPIO.cleanup() 
    
    def offRelay(self) :
        try :
            GPIO.output(self.RELAYPIN, GPIO.LOW)
        except KeyboardInterrupt :
            GPIO.cleanup
    

def main() :
    GPIOPIN = 13
    relaycommand = RelayCommand(GPIOPIN)

    relaycommand.onRelay()
    time.sleep(5)
    relaycommand.offRelay()
    time.sleep(5)

if __name__ == '__main__' :
    main()