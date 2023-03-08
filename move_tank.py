#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, LineFollowErrorTooFast, SpeedPercent, follow_for_forever
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor


def main() -> None:
    tank = MoveTank(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_B)
    tank.cs = ColorSensor(INPUT_1)

    button = TouchSensor(INPUT_3)
    button.wait_for_bump()

    try:
        tank.follow_line(
            kp=11.3, ki=0.05, kd=3.2,
            speed=SpeedPercent(30)
        )
    except LineFollowErrorTooFast:
        tank.stop()
        raise


if __name__ == '__main__':
    main()
