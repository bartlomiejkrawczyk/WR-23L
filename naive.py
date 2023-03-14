#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from time import sleep

##################
#                #
#    SETTINGS    #
#                #
##################

FORWARD_SPEED = 30
TURN_SPEED = 40

SLEEP_SECONDS = 1

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
    if left_sensor.color == right_sensor.color:
        move_tank.on(
            SpeedPercent(FORWARD_SPEED),
            SpeedPercent(FORWARD_SPEED)
        )
    elif left_sensor.color != ColorSensor.COLOR_BLACK and right_sensor.color != ColorSensor.COLOR_BLACK:
        move_tank.on(
            SpeedPercent(FORWARD_SPEED),
            SpeedPercent(FORWARD_SPEED)
        )
    elif left_sensor.color != ColorSensor.COLOR_WHITE and right_sensor.color == ColorSensor.COLOR_WHITE:
        move_tank.on(
            SpeedPercent(-FORWARD_SPEED - TURN_SPEED),
            SpeedPercent(FORWARD_SPEED + TURN_SPEED)
        )
    elif left_sensor.color == ColorSensor.COLOR_WHITE and right_sensor.color != ColorSensor.COLOR_WHITE:
        move_tank.on(
            SpeedPercent(FORWARD_SPEED + TURN_SPEED),
            SpeedPercent(-FORWARD_SPEED - TURN_SPEED)
        )
    elif left_sensor.color == ColorSensor.COLOR_NOCOLOR or right_sensor.color == ColorSensor.COLOR_NOCOLOR:
        move_tank.off()

    sleep(SLEEP_SECONDS)


def stop() -> None:
    move_tank.off()


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
