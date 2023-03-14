#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

##################
#                #
#    SETTINGS    #
#                #
##################

FORWARD_SPEED = 40
TURN_SPEED = 30
BACK_TURN_SPEED = -45
MAX_TURN_COUNT = 4

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
    forward_count = 0
    left_turn_count = 0
    right_turn_count = 0

    is_turning_left = False
    is_turning_right = False

    while True:
        if button.is_pressed:
            handle_button_pressed()
        else:
            iterate(
                forward_count,
                left_turn_count,
                right_turn_count,
                is_turning_left,
                is_turning_right
            )


def handle_button_pressed() -> None:
    stop()
    speak('STOP')
    button.wait_for_released()
    button.wait_for_bump()
    speak('START')


def iterate(forward_count: int,
            left_turn_count: int,
            right_turn_count: int,
            is_turning_left: bool,
            is_turning_right: bool) -> None:

    if isForward() and not is_turning_left and not is_turning_right:
        move_tank.on(SpeedPercent(FORWARD_SPEED), SpeedPercent(FORWARD_SPEED))
        if forward_count <= MAX_TURN_COUNT:
            forward_count += 1
            if forward_count == MAX_TURN_COUNT:
                left_turn_count = 0
                right_turn_count = 0
    elif isLeft():
        while True:
            move_tank.on(SpeedPercent(BACK_TURN_SPEED),
                         SpeedPercent(TURN_SPEED))
            if left_turn_count <= MAX_TURN_COUNT:
                left_turn_count += 1
                forward_count = 0
                if left_turn_count == MAX_TURN_COUNT:
                    is_turning_left = True

            if is_turning_left:
                if (right_sensor.color == ColorSensor.COLOR_BLACK):
                    is_turning_left = False
                    break
            elif isForward():
                break
    elif isRight():
        while True:
            move_tank.on(SpeedPercent(TURN_SPEED),
                         SpeedPercent(BACK_TURN_SPEED))
            if right_turn_count <= MAX_TURN_COUNT:
                right_turn_count += 1
                forward_count = 0
                if right_turn_count == MAX_TURN_COUNT:
                    is_turning_right = True

            if is_turning_right:
                if (left_sensor.color == 1):
                    is_turning_right = False
                    break
            elif isForward():
                break

    elif left_sensor.color == ColorSensor.COLOR_NOCOLOR or right_sensor.color == ColorSensor.COLOR_NOCOLOR:
        move_tank.off()


def isForward() -> bool:
    return left_sensor.color == right_sensor.color or left_sensor.color != ColorSensor.COLOR_BLACK and right_sensor.color != ColorSensor.COLOR_BLACK


def isLeft() -> bool:
    return left_sensor.color != ColorSensor.COLOR_WHITE and right_sensor.color == ColorSensor.COLOR_WHITE


def isRight() -> bool:
    return left_sensor.color == ColorSensor.COLOR_WHITE and right_sensor.color != ColorSensor.COLOR_WHITE


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
