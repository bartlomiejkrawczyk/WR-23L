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

MIN_FORWARD_SPEED = 10
MAX_FORWARD_SPEED = 20

FORWARD_SPEED_CORRECTION = (
    (MAX_FORWARD_SPEED - MIN_FORWARD_SPEED) / MAX_FORWARD_SPEED
)

CONSTANT_P = 4.0
CONSTANT_I = 0.01
CONSTANT_D = 4.0

HISTORY_LOSS = 0.5

AMPLIFIER = 0.25

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

# move_tank = MoveTank(OUTPUT_A, OUTPUT_B)

######################
#                    #
#    MAIN PROGRAM    #
#                    #
######################


def speak(message: str) -> None:
    sound.speak(message)
    print(message)


def work() -> None:
    integral = 0.0
    last_error = 0

    while True:
        if button.is_pressed:
            handle_button_pressed()
        else:
            try:
                integral, last_error = iterate(integral, last_error)
            except Exception as e:
                print(e)


def handle_button_pressed() -> None:
    stop()
    speak('STOP')
    button.wait_for_released()
    button.wait_for_bump()
    speak('START')


def iterate(integral: float, last_error: int) -> Tuple[float, int]:
    error = left_sensor.reflected_light_intensity - \
        right_sensor.reflected_light_intensity

    integral = HISTORY_LOSS * integral + error
    derivative = error - last_error
    last_error = error

    turn_speed = CONSTANT_P * error + CONSTANT_I * integral + CONSTANT_D * derivative

    forward_speed = max(
        MIN_FORWARD_SPEED,
        MAX_FORWARD_SPEED - FORWARD_SPEED_CORRECTION * abs(turn_speed)
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
