import RPi.GPIO as gpio
import time

leftRed = 11
leftBlack = 13
leftEnable = 31
rightRed = 21
rightBlack = 23
rightEnable = 33

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(leftRed, gpio.OUT)
    gpio.setup(leftBlack, gpio.OUT)
    gpio.setup(leftEnable, gpio.OUT)
    gpio.setup(rightRed, gpio.OUT)
    gpio.setup(rightBlack, gpio.OUT)
    gpio.setup(rightEnable, gpio.OUT)
    turnStraight()

def turnLeft():
    gpio.output(leftEnable, gpio.LOW)
    gpio.output(rightEnable, gpio.HIGH)

def turnRight():
    gpio.output(leftEnable, gpio.HIGH)
    gpio.output(rightEnable, gpio.LOW)

def turnStraight():
    gpio.output(leftEnable, gpio.HIGH)
    gpio.output(rightEnable, gpio.HIGH)

def forward():
    gpio.output(leftRed, gpio.HIGH)
    gpio.output(leftBlack, gpio.LOW)
    gpio.output(rightRed, gpio.LOW)
    gpio.output(rightBlack, gpio.HIGH)

def backward():
    gpio.output(leftRed, gpio.LOW)
    gpio.output(leftBlack, gpio.HIGH)
    gpio.output(rightRed, gpio.HIGH)
    gpio.output(rightBlack, gpio.LOW)

def stop():
    gpio.output(leftRed, gpio.LOW)
    gpio.output(leftBlack, gpio.LOW)
    gpio.output(rightRed, gpio.LOW)
    gpio.output(rightBlack, gpio.LOW)

def cleanup():
    gpio.cleanup()

if __name__ == '__main__':
    try:
        setup()
        forward()
        time.sleep(1)
        turnLeft()
        time.sleep(1)
        turnRight()
        time.sleep(1)
        stop()
        time.sleep(1)
        turnStraight()
        backward()
        time.sleep(1)
    except BaseException, e:
        print(e)
    finally:
        gpio.cleanup()



