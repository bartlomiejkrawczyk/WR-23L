#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

SPEED_STRAIGHT = 30
SPEED_TURN = 30


def iteration(tank: MoveTank, left: ColorSensor, right: ColorSensor) -> None:

    if left.color == ColorSensor.COLOR_WHITE and right.color == ColorSensor.COLOR_WHITE:
        tank.on(left_speed=SPEED_STRAIGHT, right_speed=SPEED_STRAIGHT)
    elif left.color == ColorSensor.COLOR_BLACK and right.color == ColorSensor.COLOR_BLACK:
        tank.on(left_speed=SPEED_STRAIGHT, right_speed=SPEED_STRAIGHT)
    elif left.color == ColorSensor.COLOR_BLACK and right.color == ColorSensor.COLOR_WHITE:
        tank.on(left_speed=-SPEED_TURN, right_speed=SPEED_TURN)
    elif left.color == ColorSensor.COLOR_WHITE and right.color == ColorSensor.COLOR_BLACK:
        tank.on(left_speed=SPEED_TURN, right_speed=-SPEED_TURN)


def loop(tank: MoveTank, left: ColorSensor, right: ColorSensor) -> None:
    while True:
        iteration(tank, left, right)


def main() -> None:
    tank = MoveTank(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_B)
    color_sensor_left = ColorSensor(INPUT_1)
    color_sensor_right = ColorSensor(INPUT_2)

    button = TouchSensor(INPUT_3)
    button.wait_for_bump()

    try:
        loop(tank, color_sensor_left, color_sensor_right)
    except KeyboardInterrupt:
        tank.stop()
        raise


if __name__ == '__main__':
    main()
