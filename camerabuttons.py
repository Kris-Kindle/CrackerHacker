import time
import picamera
import RPi.GPIO as GPIO

# Sets GPIO pins to match pinout on Cobbler board
GPIO.setmode(GPIO.BCM)

# Set up each of the pins so that we can call them later
GPIO.setup(4, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

def picture_time(x):
    photo = x + "/" + time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime()) + ".jpg"
    return(photo)

# Initialize the camera
camera = picamera.PiCamera()

while True:
    input_state1 = GPIO.input(4)
    if input_state1 == True:
        camera.capture(picture_time("Ritz"))
        time.sleep(1)
        print("You took a picture of a Ritz cracker")
    input_state2 = GPIO.input(18)
    if input_state2 == True:
        camera.capture(picture_time("Townhouse"))
        time.sleep(1)
        print("You took a picture of a Townhouse cracker")
    input_state3 = GPIO.input(17)
    if input_state3 == True:
        camera.capture(picture_time("Triscuits"))
        time.sleep(1)
        print("You took a picture of a Triscuit cracker")
    input_state4 = GPIO.input(27)
    if input_state4 == True:
        camera.capture(picture_time("WheatThins"))
        time.sleep(1)
        print("You took a picture of a Wheat Thins cracker")
    input_state5 = GPIO.input(22)
    if input_state5 == True:
        camera.capture(picture_time("Cheeseits"))
        time.sleep(1)
        print("You took a picture of a Cheeseits cracker")
    input_state6 = GPIO.input(23)
    if input_state6 == True:
        camera.capture(picture_time("Saltines"))
        time.sleep(1)
        print("You took a picture of a Saltine cracker")
    input_state7 = GPIO.input(24)
    if input_state7 == True:
        camera.capture(picture_time("Matzahs"))
        time.sleep(1)
        print("You took a picture of a Matzah cracker")

