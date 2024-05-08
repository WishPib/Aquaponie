import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en = 18 #peut être GPIO 12,13,18 ou 19 car PWM

def pomperEau(direction, pwmPercent):
    if direction :
        GPIO.output(in1, GPIO.HIGH)  
        GPIO.output(in2, GPIO.LOW)
        pwm.ChangeDutyCycle(pwmPercent)
        sleep(2)
    else :
        GPIO.output(in1, GPIO.LOW)  
        GPIO.output(in2, GPIO.HIGH)
        pwm.ChangeDutyCycle(pwmPercent)
        sleep(2)

def pomperEau(direction):
    if direction :
        GPIO.output(in1, GPIO.HIGH)  
        GPIO.output(in2, GPIO.LOW)
        pwm.ChangeDutyCycle(100)
        sleep(2)
    else :
        GPIO.output(in1, GPIO.LOW)  
        GPIO.output(in2, GPIO.HIGH)
        pwm.ChangeDutyCycle(100)
        sleep(2)
        
def stop():
    GPIO.output(in1, GPIO.LOW)  
    GPIO.output(in2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    sleep(2)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.HIGH)
pwm = GPIO.PWM(en,100)
pwm.start(0)

