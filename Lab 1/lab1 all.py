import RPi.GPIO as GPIO
import time
import sys
mode = GPIO.getmode()

# Pin define
status_LED = 19
headlights = 12, 26
buzzer = 16
motor1_forward = 0
motor1_backward = 5
motor2_forward = 7
motor2_backward = 6

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configure the pin as an output
GPIO.setup(status_LED, GPIO.OUT)
GPIO.setup(headlights, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(motor1_forward, GPIO.OUT)
GPIO.setup(motor1_backward, GPIO.OUT)
GPIO.setup(motor2_forward, GPIO.OUT)
GPIO.setup(motor2_backward, GPIO.OUT)

beep = GPIO.PWM(buzzer, 500)

def status_LED_on():
    # Turn ON the status LED
    GPIO.output(status_LED,GPIO.HIGH)
    # Keep the LED on for 2 second

    time.sleep(2)
    # Turn OFF the status LED
    GPIO.output(status_LED,GPIO.LOW)
           
def buzzer_on():  
    beep.start(50)          
    time.sleep(2)  
    beep.stop()
            
#cleanup function
def cleanup():
    GPIO.output(motor1_forward, GPIO.LOW)
    GPIO.output(motor1_backward, GPIO.LOW)
    GPIO.output(motor2_forward, GPIO.LOW)
    GPIO.output(motor2_backward, GPIO.LOW)
    GPIO.output(status_LED,GPIO.LOW)
    GPIO.output(headlights,GPIO.LOW)

def forward(x):
    GPIO.output(headlights,GPIO.HIGH)
    GPIO.output(motor1_forward, GPIO.HIGH)
    GPIO.output(motor2_forward, GPIO.HIGH)
    print("motors running forward")
    time.sleep(x)
    GPIO.output(motor1_forward, GPIO.LOW)
    GPIO.output(motor2_forward, GPIO.LOW)
    GPIO.output(headlights, GPIO.LOW)

def backward(x):
    GPIO.output(headlights,GPIO.HIGH)
    GPIO.output(motor1_backward, GPIO.HIGH)
    GPIO.output(motor2_backward, GPIO.HIGH)
    print("motors running backward")
    time.sleep(x)
    GPIO.output(motor1_backward, GPIO.LOW)
    GPIO.output(motor2_backward, GPIO.LOW)
    GPIO.output(headlights, GPIO.LOW)

try:
    status_LED_on()
    buzzer_on()
    forward(2)
    buzzer_on()
    backward(2)

except Keyboardinterrupt:
    GPIO.cleanup()
    exit(1)
    
cleanup()
exit(0)
    