#!/usr/bin/python
#import Raspi_MotorHAT, Raspi_DCMotor, Raspi_Stepper 
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor, Raspi_StepperMotor

import time
import atexit
import curses


screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)


mh = Raspi_MotorHAT(0x6F)

#This code turns off the motors when the program is exited.
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

Stepper1 = mh.getStepper(200, 1)  	# 200 steps/rev, motor port #1
Stepper1.setSpeed(15)  		        # 30 RPM

Stepper2 = mh.getStepper(200, 2)  	# 200 steps/rev, motor port #2
Stepper2.setSpeed(30)  		        # 30 RPM
 		# 30 RPM

#Below is just a simple while loop that turns the motors in the corresponding direction to whichever key is entered
#on the keyboard. 

try:
    while (True):
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
                Stepper1.step(10, Raspi_MotorHAT.FORWARD,  Raspi_MotorHAT.INTERLEAVE)

        elif char == curses.KEY_DOWN:
                Stepper1.step(10, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.INTERLEAVE)

        elif char == curses.KEY_RIGHT:
                Stepper2.step(10, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.INTERLEAVE)
        elif char == curses.KEY_LEFT:
                Stepper2.step(10, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.INTERLEAVE)
                 


                
                


	

finally:
   
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


