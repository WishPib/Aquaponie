import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en = 18 #peut être GPIO 12,13,18 ou 19 car PWM

def pomper():
    GPIO.output(in1, GPIO.LOW)  
    GPIO.output(in2, GPIO.HIGH)
    pwm.ChangeDutyCycle(50)
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


while(True):
    # pomper dans une direction (inverser les inputs pour l'autre direction)
    GPIO.output(in1, GPIO.LOW)  
    GPIO.output(in2, GPIO.HIGH)
    pwm.ChangeDutyCycle(50) # % de puissance    
    sleep(2) # NB de secondes ou le sys fait rien   
