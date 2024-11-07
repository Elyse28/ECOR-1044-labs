import RPi.GPIO as GPIO
import time

#Buzzer Stuff
           
# Set the buzzer pin as an output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Buzzer pin
buzzer = 16

#set buzzer pin as output
GPIO.setup(buzzer, GPIO.OUT)
            
beep = GPIO.PWM(buzzer, 500)

beep.start(50)
            
time.sleep(2)
    
beep.stop
            
GPIO.cleanup()