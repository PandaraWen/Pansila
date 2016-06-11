from evdev import InputDevice
from select import select
import engine
import RPi.GPIO as gpio

keyForward = 16 #q
keyBackward = 30 #a
keyLeft = 24 #o
keyRight = 25 #p

vKeyPress = 1
vKeyRelease = 0
vKeyHold = 2

dev = InputDevice('/dev/input/event0')

def setup():
    engine.setup()
    engine.stop()
    engine.turnStraight()

def printKeyboard():
    while True:
        select([dev], [], [])
        for event in dev.read():
                if event.value == 1:
                    print "Key is :%s" % event.code

def observeKeyboard():
    while True:
        select([dev], [], [])
        for event in  dev.read():
            if event.code == keyForward:#forward
                if event.value == vKeyPress:
                    engine.forward()
                elif event.value == vKeyRelease:
                    engine.stop()
            elif event.code == keyBackward:#backward
                if event.value == vKeyPress:
                    engine.backward()
                elif event.value == vKeyRelease:
                    engine.stop()
            elif event.code == keyLeft:#left
                if event.value == vKeyPress:
                    engine.turnLeft()
                elif event.value == vKeyRelease:
                    engine.turnStraight()
            elif event.code == keyRight:#right
                if event.value == vKeyPress:
                    engine.turnRight()
                elif event.value == vKeyRelease:
                    engine.turnStraight()

def cleanup():
    gpio.cleanup()

if __name__ == '__main__':
    try:
        setup()
        observeKeyboard()
    except BaseException, e:
        print(e)
    finally:
        cleanup() 

