#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from time import sleep
from threading import Thread
from typing import List

LEFT = 0
RIGHT = 1

FORWARD_SPEED = 30

ERROR_MULTIPLIER = 11.3
INTEGRAL_MULTIPLIER = 0.05
DERIVATIVE_MULTIPLIER = 3.2

HISTORY_LOSS_SPEED = 0.9

SOUND_VOLUME = 100
INSIGNIFICANT_READ_FREQUENCY_HZ = 4

insignificant_read_every_ms = int(1_000 / INSIGNIFICANT_READ_FREQUENCY_HZ)


class LineFollower:
    _wheels: List[LargeMotor]
    _color_sensors: List[ColorSensor]

    _follow_line: bool

    _forward_speed: int
    _turn_speed: List[int]

    _integral: float = 0.0
    _last_error: float = 0.0
    _derivative: float = 0.0

    def __init__(
        self,
        wheel_pins: List[str] = [OUTPUT_A, OUTPUT_B],
        color_sensor_pins: List[str] = [INPUT_1, INPUT_2]
    ) -> None:
        self._wheels: List[LargeMotor] = [
            LargeMotor(pin) for pin in wheel_pins
        ]
        self._color_sensors: List[ColorSensor] = [
            ColorSensor(pin) for pin in color_sensor_pins
        ]
        self._follow_line: bool = False
        self._forward_speed = FORWARD_SPEED
        self._turn_speed: List[int] = [0, 0]

    def start(self) -> None:
        self._follow_line = True

    def stop(self) -> None:
        self._follow_line = False

        sleep(insignificant_read_every_ms)

        for wheel in self._wheels:
            wheel.stop()

    def work(self) -> None:
        while True:
            if self._follow_line:
                self._read_sensors()
                self._update_wheel_speed()
            else:
                sleep(insignificant_read_every_ms)

    def _read_sensors(self) -> None:
        left_read = self._color_sensors[LEFT].reflected_light_intensity
        right_read = self._color_sensors[RIGHT].reflected_light_intensity

        self._error = left_read - right_read
        self._integral = HISTORY_LOSS_SPEED * self._integral + self._error
        self._derivative = self._error - self._last_error

        self._last_error = self._error

        turn_speed = int(
            ERROR_MULTIPLIER * self._error +
            INTEGRAL_MULTIPLIER * self._integral +
            DERIVATIVE_MULTIPLIER * self._derivative
        )

        self._turn_speed = [
            turn_speed,
            -turn_speed
        ]

    def _update_wheel_speed(self) -> None:
        for wheel, turn_speed in zip(self._wheels, self._turn_speed):
            calculated_speed = self._forward_speed + turn_speed
            rounded = max(min(calculated_speed, 100), -100)
            wheel.on(rounded)


def register_button(robot: LineFollower, pin: str = INPUT_1) -> Thread:
    button = TouchSensor(pin)
    thread = Thread(target=initialize_button, args=(robot, button))
    thread.start()
    return thread


def initialize_button(robot: LineFollower, button: TouchSensor) -> None:
    sound = Sound()
    sound.set_volume(SOUND_VOLUME)
    sound.speak('Ready')
    print('READY')

    while True:
        button.wait_for_bump(sleep_ms=insignificant_read_every_ms)
        sound.speak('Start')
        print('START')
        robot.start()

        button.wait_for_bump(sleep_ms=insignificant_read_every_ms)
        sound.speak('Stop')
        print('STOP')
        robot.stop()


def main() -> None:
    robot = LineFollower()

    register_button(robot)

    try:
        robot.work()
    except KeyboardInterrupt as e:
        robot.stop()
        raise e


if __name__ == '__main__':
    main()
