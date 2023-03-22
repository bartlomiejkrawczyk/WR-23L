#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from typing import Tuple

from time import sleep

##################
#                #
#    SETTINGS    #
#                #
##################

MIN_FORWARD_SPEED = 10
MAX_FORWARD_SPEED = 20

###################
#                 #
#    CONSTANTS    #
#                 #
###################

SOUND_VOLUME = 100

LEFT = 0
RIGHT = 1

FROM = ColorSensor.COLOR_RED
TO = ColorSensor.COLOR_GREEN

#####################
#                   #
#    PERIPHERALS    #
#                   #
#####################

sound = Sound()
button = TouchSensor(INPUT_3)

left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)

motors = [left_motor, right_motor]

left_sensor = ColorSensor(INPUT_1)
right_sensor = ColorSensor(INPUT_2)

sensors = [left_sensor, right_sensor]


################
#              #
#    STATES    #
#              #
################

FOLLOW_LINE_UNTIL_FROM = 0
FOLLOW_LINE_UNTIL_TO = 1
FOLLOW_LINE_UNTIL_DETECTED_OBJECT = 2
TURN_LEFT = 10
TURN_RIGHT = 11

######################
#                    #
#    MAIN PROGRAM    #
#                    #
######################


def speak(message: str) -> None:
    sound.speak(message)
    print(message)


def work() -> None:
    state = FOLLOW_LINE_UNTIL_FROM
    desired_color = FROM

    while True:
        if button.is_pressed:
            handle_button_pressed()
        else:
            state, desired_color = iterate(state, desired_color)


def iterate(state: int, desired_color: int) -> Tuple[int, int]:
    colors = detect_colors()

    desired_color = 1

    if state == FOLLOW_LINE_UNTIL_FROM:
        if colors[LEFT] == FROM:
            state = TURN_LEFT
        elif colors[RIGHT] == FROM:
            state = TURN_RIGHT
    elif state == TURN_LEFT:
        if colors[RIGHT] == desired_color:
            state = FOLLOW_LINE_UNTIL_DETECTED_OBJECT
    elif state == TURN_RIGHT:
        if colors[LEFT] == desired_color:
            state = FOLLOW_LINE_UNTIL_DETECTED_OBJECT
    
    print('colors = ', colors)
    print('state = ', state)
    

    if state in [FOLLOW_LINE_UNTIL_FROM, FOLLOW_LINE_UNTIL_TO, FOLLOW_LINE_UNTIL_DETECTED_OBJECT]:
        try:
            follow_line()
        except Exception as e:
            print(e)
    elif state == TURN_RIGHT:
        left_motor.on(-MIN_FORWARD_SPEED)
        right_motor.on(MIN_FORWARD_SPEED)
    elif state == TURN_LEFT:
        left_motor.on(MIN_FORWARD_SPEED)
        right_motor.on(MIN_FORWARD_SPEED)

    return state, desired_color


def handle_button_pressed() -> None:
    stop()
    speak('STOP')
    button.wait_for_released()
    button.wait_for_bump()
    speak('START')


def detect_colors() -> Tuple[int, int]:
    left_sensor.mode = ColorSensor.MODE_COL_COLOR
    right_motor.mode = ColorSensor.MODE_COL_COLOR
    return (
        left_sensor.color,
        right_sensor.color
    )


def follow_line() -> None:
    colors = (
        left_sensor.color,
        right_sensor.color
    )
    if colors[LEFT] == colors[RIGHT]:
        left_motor.on(MIN_FORWARD_SPEED)
        right_motor.on(MIN_FORWARD_SPEED)
    elif colors[LEFT] != ColorSensor.COLOR_BLACK and colors[RIGHT] != ColorSensor.COLOR_BLACK:
        left_motor.on(MIN_FORWARD_SPEED)
        right_motor.on(MIN_FORWARD_SPEED)
    elif colors[LEFT] != ColorSensor.COLOR_WHITE and colors[RIGHT] == ColorSensor.COLOR_WHITE:
        left_motor.on(-MIN_FORWARD_SPEED)
        right_motor.on(MIN_FORWARD_SPEED)
    elif colors[LEFT] == ColorSensor.COLOR_WHITE and colors[RIGHT] != ColorSensor.COLOR_WHITE:
        left_motor.on(MIN_FORWARD_SPEED)
        right_motor.on(-MIN_FORWARD_SPEED)
    elif colors[LEFT] == ColorSensor.COLOR_NOCOLOR or colors[RIGHT] == ColorSensor.COLOR_NOCOLOR:
        left_motor.on(0)
        right_motor.on(0)

def stop() -> None:
    for motor in motors:
        motor.stop()


def main() -> None:
    sound.set_volume(SOUND_VOLUME)
    speak('READY')

    button.wait_for_bump()
    speak('START')

    try:
        work()
    except KeyboardInterrupt as e:
        stop()
        raise e


if __name__ == '__main__':
    main()
