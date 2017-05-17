from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


class steering_motor:
    def __init__(self, controller, pwm_pin, sleep_pin, dir_pin, flt_pin):
        self.MC = controller
        if (pwm_pin < 0) or (pwm_pin > 15):
            raise NameError('PWM pin must be between 0 and 15 inclusive')

        self.pwm_pin = pwm_pin
        self.sleep_pin = sleep_pin
        GPIO.setup(sleep_pin, GPIO.OUT)

        self.dir_pin = dir_pin
        GPIO.setup(dir_pin, GPIO.OUT)

        self.flt_pin = flt_pin
        GPIO.setup(flt_pin, GPIO.IN)


    def setSpeed(self, speed):
        if (speed < 0):
            speed = 0
        if (speed > 255):
            speed = 255
        self.MC._pwm.setPWM(self.pwm_pin, 0, speed*16)
    def testSpeed(self, speed):
        GPIO.output(self.sleep_pin, 1)
        self.setSpeed(speed)
        time.sleep(1)
        GPIO.output(self.sleep_pin, 0)


mh = Adafruit_MotorHAT()
motor = steering_motor(mh, 15, 23, 22, 24)

def setSpeed(speed):
    motor.setSpeed(speed)

def testSpeed(speed):
    motor.testSpeed(speed)
if __name__ == "__main__":
    motor.setSpeed(10)
