#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# INFORMATION FOR ROBOT
EV3 = EV3Brick()
COLOR_SENSOR_RIGHT = ColorSensor(Port.S4) 
COLOR_SENSOR_LEFT = ColorSensor(Port.S1)
DISTANCE_SENSOR = UltrasonicSensor(Port.S2)  
TOUCH_SENSOR = TouchSensor(Port.S3)
LEFT_MOTOR_PORT = Port.B
RIGHT_MOTOR_PORT = Port.C
WHEEL_DIAMETER = 56 
AXLE_TRACK = 145 
ROBOT = DriveBase(Motor(LEFT_MOTOR_PORT), Motor(RIGHT_MOTOR_PORT), WHEEL_DIAMETER, AXLE_TRACK)

# GLOBAL VARIABLES
RED = 10
GREEN = 10
BLUE = 10
execute_program = True
pause_numbers = 0
last_time = time.time()

# FUNCTIONS FOR ENTERTAINMENT
def sarias_theme():
    NOTES = ['F4/1', 'A4/1', 'B4/2', 'F4/1', 'A4/1', 'B4/2', 'F4/1', 'A4/1', 'B4/1', 'E5/1', 'D5/2', 'B4/1', 'C5/1', 'B4/1', 'G4/1', 'E4/6']
    EV3.speaker.play_notes(NOTES, tempo = 150*4)

def sotime():
    NOTES = ['A4/2', 'D4/4', 'F4/2', 'A4/2', 'D4/4', 'F4/2', 'A4/1', 'C5/1', 'B4/2', 'G4/2', 'F4/1', 'G4/1', 'A4/2', 'D4/2', 'C4/1', 'E4/1', 'D4/2']
    EV3.speaker.play_notes(NOTES, tempo = 150*4)

def lullaby():
    NOTES = ['B4/4', 'D5/2', 'A4/6', 'B4/4', 'D5/2', 'A4/6', 'B4/4', 'D5/2', 'A5/4', 'G5/2', 'D5/12']
    EV3.speaker.play_notes(NOTES, tempo= 92*4)

def epona():
    NOTES = ['D5/1', 'B4/1', 'A4/4', 'D5/1', 'B4/1', 'A4/4', 'D5/1', 'B4/1', 'A4/2', 'B4/2']
    EV3.speaker.play_notes(NOTES, tempo = 108*4)

def underhold_publikum():
    wait(2000)
    r = random.randint(1, 4)
    if r == 1:
        sarias_theme()
    elif r == 2:
        sotime()
    elif r == 3:
        lullaby()
    elif r == 4:
        epona()

#soundfile.play('sounds/587924__josefpres__bass-loops-031-with-drums-short-loop-120-bpm.wav')
# START DRIVING ON THAT FRIMERKE
while execute_program:
    ROBOT.drive(100,0)
    (red_left, green_left, blue_left) = COLOR_SENSOR_LEFT.rgb()
    (red_right, green_right, blue_right) = COLOR_SENSOR_RIGHT.rgb()
    is_black_left = red_left < RED or green_left < GREEN or blue_left < BLUE
    is_black_right = red_right < RED or green_right < GREEN or blue_right < BLUE

    while is_black_left: #If the left sensor sees the black tape, then the car will turn as to drive correctly
        ROBOT.turn(-15)
        (red_left, green_left, blue_left) = COLOR_SENSOR_LEFT.rgb()
        is_black_left = red_left < RED or green_left < GREEN or blue_left < BLUE
        EV3.screen.print("LEFT")
    while is_black_right: #If the right sensor sees the black tape, then the car will turn as to drive correctly
        ROBOT.turn(15)
        (red_right, green_right, blue_right) = COLOR_SENSOR_RIGHT.rgb()
        is_black_right = red_right < RED or green_right < GREEN or blue_right < BLUE
        EV3.screen.print("RIGHT")

    current_time = time.time()
    if current_time - last_time>=10:
        ROBOT.drive(0,0)

        underhold_publikum()
        pause_numbers += 1
        last_time = time.time()
    if DISTANCE_SENSOR.distance()<150:
        ROBOT.drive(0,0)
        EV3.speaker.play_file(SoundFile.FANFARE)
        execute_program = False
    if pause_numbers>=5:
        execute_program = False

    
