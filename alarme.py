import RPi.GPIO as GPIO
import time

class AlarmeCommand :
    
    def __init__(self, pin) :
        self.BUZZERPIN = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)         
        GPIO.setup(self.BUZZERPIN, GPIO.OUT)
    
    def onAlarm(self):
        try:
            GPIO.output(self.BUZZERPIN, GPIO.HIGH)
            #state = GPIO.input(self.RELAYPIN)
        except KeyboardInterrupt:  # Interruption avec 'Ctrl+C'
            GPIO.cleanup() 
    
    def offAlarm(self) :
        try :
            GPIO.output(self.BUZZERPIN, GPIO.LOW)
        except KeyboardInterrupt :
            GPIO.cleanup
    

def main() :
    GPIOPIN = 21
    alarmecommand = AlarmeCommand(GPIOPIN)

    alarmecommand.onRelay()
    time.sleep(5)
    alarmecommand.offRelay()
    time.sleep(5)

if __name__ == '__main__' :
    main()