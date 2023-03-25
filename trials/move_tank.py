#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, LineFollowErrorTooFast, follow_for_ms  # type: ignore

##################
#                #
#    SETTINGS    #
#                #
##################

CONSTANT_P = 11.3
CONSTANT_I = 0.05
CONSTANT_D = 3.2

SPEED_PERCENT = SpeedPercent(30)

CHECK_BUTTON_INTERVAL_MS = 1000

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

left_sensor = ColorSensor(INPUT_1)
right_sensor = ColorSensor(INPUT_2)

sensors = [left_sensor, right_sensor]

move_tank = MoveTank(OUTPUT_A, OUTPUT_B)

######################
#                    #
#    MAIN PROGRAM    #
#                    #
######################


def speak(message: str) -> None:
    sound.speak(message)
    print(message)


def work() -> None:
    while True:
        if button.is_pressed:
            handle_button_pressed()
        else:
            iterate()


def handle_button_pressed() -> None:
    stop()
    speak('STOP')
    button.wait_for_released()
    button.wait_for_bump()
    speak('START')


def iterate() -> None:
    try:
        move_tank.follow_line(
            kp=CONSTANT_P,
            ki=CONSTANT_I,
            kd=CONSTANT_D,
            speed=SPEED_PERCENT,
            follow_for=follow_for_ms,  # type: ignore
            ms=CHECK_BUTTON_INTERVAL_MS
        )
    except LineFollowErrorTooFast:
        move_tank.stop()
        raise


def stop() -> None:
    move_tank.stop()


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
