import RPi.GPIO as GPIO
import time
import sys

mode = GPIO.getmode()

#motor pins
motor1_forward = 5
motor1_backward = 0
motor2_forward = 7
motor2_backward = 6
runtime = 1

#setup gpio mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#configure motor pin outputs
GPIO.setup(motor1_forward, GPIO.OUT)
GPIO.setup(motor1_backward, GPIO.OUT)
GPIO.setup(motor2_forward, GPIO.OUT)
GPIO.setup(motor2_backward, GPIO.OUT)
            
#cleanup function
def cleanup():
    GPIO.output(motor1_forward, GPIO.LOW)
    GPIO.output(motor1_backward, GPIO.LOW)
    GPIO.output(motor2_forward, GPIO.LOW)
    GPIO.output(motor2_backward, GPIO.LOW)

def forward_backward (x):
    GPIO.output(motor1_forward, GPIO.HIGH)
    GPIO.output(motor2_forward, GPIO.HIGH)
    print("motors running forward")
    time.sleep(x)
    GPIO.output(motor1_forward, GPIO.LOW)
    GPIO.output(motor2_forward, GPIO.LOW)
    GPIO.output(motor1_backward, GPIO.HIGH)
    GPIO.output(motor2_backward, GPIO.HIGH)
    print("motors running backward")
    time.sleep(x)
    GPIO.output(motor1_backward, GPIO.LOW)
    GPIO.output(motor2_backward, GPIO.LOW)

try:
    forward_backward(2)

except Keyboardinterrupt:
    GPIO.cleanup()
    exit(1)

cleanup()
exit(0)