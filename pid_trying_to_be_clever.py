#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from typing import Tuple

##################
#                #
#    SETTINGS    #
#                #
##################

FORWARD_LINE_SPEED = 100
FORWARD_SPEED = 25

CONSTANT_P = 4.15
CONSTANT_I = 2.01
CONSTANT_D = 4.2

HISTORY_LOSS = 0.5

AMPLIFIER = 0.05

###################
#                 #
#    CONSTANTS    #
#                 #
###################

SOUND_VOLUME = 100

LEFT = 0
RIGHT = 1

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

######################
#                    #
#    MAIN PROGRAM    #
#                    #
######################


def speak(message: str) -> None:
    sound.speak(message)
    print(message)


def work() -> None:
    integral = (0.0, 0.0)
    last_error = 0
    expected = configure()
    while True:
        if button.is_pressed:
            handle_button_pressed()
            expected = configure()
        else:
            integral, last_error = iterate(integral, last_error, expected)


def configure() -> Tuple[int, int]:
    return left_sensor.reflected_light_intensity, right_sensor.reflected_light_intensity


def handle_button_pressed() -> None:
    stop()
    speak('STOP')
    button.wait_for_released()
    button.wait_for_bump()
    speak('START')


def iterate(integral: Tuple[float, float], last_error: int, expected: Tuple[int, int]) -> Tuple[Tuple[float, float], int]:
    if left_sensor.color == ColorSensor.COLOR_WHITE and right_sensor.color == ColorSensor.COLOR_WHITE:
        forward_speed = FORWARD_LINE_SPEED
    else:
        forward_speed = FORWARD_SPEED

    error = (
        left_sensor.reflected_light_intensity - expected[LEFT],
        right_sensor.reflected_light_intensity - expected[RIGHT]
    )

    integral = (
        HISTORY_LOSS * integral[LEFT] + error[LEFT],
        HISTORY_LOSS * integral[RIGHT] + error[RIGHT]
    )

    temp_error = error[LEFT] - error[RIGHT]
    derivative = temp_error - last_error
    last_error = temp_error

    turn_speed = (
        CONSTANT_P * temp_error
        + CONSTANT_I * (integral[LEFT] - integral[RIGHT])
        + CONSTANT_D * derivative
    )

    left_motor.on(forward_speed + AMPLIFIER * turn_speed)
    right_motor.on(forward_speed - AMPLIFIER * turn_speed)

    return integral, last_error


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
