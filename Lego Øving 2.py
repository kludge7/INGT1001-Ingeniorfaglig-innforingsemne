#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()

# Initialize the sensors.
obstacle_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S3)

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=145)

# Start mowing lawn
while not touch_sensor.pressed():
    continue

ev3.speaker.say("Exercise 2")
wait(2000)

while not touch_sensor.pressed():
    robot.drive(200,0)
    while obstacle_sensor.distance()>300:
        wait(10)
    robot.straight(-400)
    robot.turn(60)

ev3.speaker.say("Exercise done")
wait(2000)
