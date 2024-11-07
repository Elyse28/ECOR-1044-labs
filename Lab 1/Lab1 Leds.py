import RPi.GPIO as GPIO
import time

status_LED = 19
headlights = 12, 26
# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Configure the pin as an output
GPIO.setup(status_LED, GPIO.OUT)
GPIO.setup(headlights, GPIO.OUT)
# Turn ON the status LED
GPIO.output(status_LED,GPIO.HIGH)
GPIO.output(headlights,GPIO.HIGH)
# Keep the LED on for 2 second
time.sleep(2)
# Turn OFF the status LED
GPIO.output(status_LED,GPIO.LOW)
GPIO.output(headlights,GPIO.LOW)

# Clean up the GPIO setting
GPIO.cleanup()