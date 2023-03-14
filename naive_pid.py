#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from typing import List, Tuple

##################
#                #
#    SETTINGS    #
#                #
##################

CONSTANT_P = 4.15
CONSTANT_I = 2.01
CONSTANT_D = 4.2

HISTORY_LOSS = 0.5
AMPLIFIER = 2

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
    last_error = [0, 0]
    integral = [0.0, 0.0]
    while True:
        if button.is_pressed:
            handle_button_pressed()
        else:
            last_error, integral = iterate(last_error, integral)


def handle_button_pressed() -> None:
    stop()
    speak('STOP')
    button.wait_for_released()
    button.wait_for_bump()
    speak('START')


def iterate(last_error: List[int], integral: List[float]) -> Tuple[List[int], List[float]]:
    color = [left_sensor.color, right_sensor.color]
    error = [color[LEFT] - ColorSensor.COLOR_WHITE,
             color[RIGHT] - ColorSensor.COLOR_WHITE]

    if color[LEFT] == ColorSensor.COLOR_WHITE and color[RIGHT] == ColorSensor.COLOR_WHITE:
        base_speed = 100
    else:
        base_speed = 25

    if not (color[LEFT] != ColorSensor.COLOR_BLACK and color[LEFT] != ColorSensor.COLOR_WHITE) or (color[RIGHT] != ColorSensor.COLOR_BLACK and color[RIGHT] != ColorSensor.COLOR_WHITE):
        integral = [
            HISTORY_LOSS * integral[LEFT] + error[LEFT],
            HISTORY_LOSS * integral[RIGHT] + error[RIGHT]
        ]
        derivative = [
            error[LEFT] - last_error[LEFT],
            error[RIGHT] - last_error[RIGHT]
        ]
        adjustment = [
            CONSTANT_P * error[LEFT]
            + CONSTANT_I * integral[LEFT]
            + CONSTANT_D * derivative[LEFT],
            CONSTANT_P * error[RIGHT]
            + CONSTANT_I * integral[RIGHT]
            + CONSTANT_D * derivative[RIGHT]
        ]

        left_motor.run_forever(
            speed_sp=round(
                base_speed
                - AMPLIFIER * adjustment[RIGHT]
                + AMPLIFIER * adjustment[LEFT]
            ),
            stop_action='coast'
        )
        right_motor.run_forever(
            speed_sp=round(
                base_speed
                - AMPLIFIER * adjustment[LEFT]
                + AMPLIFIER * adjustment[RIGHT]
            ),
            stop_action='coast'
        )

    last_error = error

    return last_error, integral


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
