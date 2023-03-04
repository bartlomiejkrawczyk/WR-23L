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

SOUND_VOLUME = 100
INSIGNIFICANT_READ_FREQUENCY_HZ = 4

insignificant_read_every_ms = int(1_000 / INSIGNIFICANT_READ_FREQUENCY_HZ)


class LineFollower:
    _wheels: List[LargeMotor]
    _color_sensors: List[ColorSensor]

    _work: bool

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
        self._work: bool = False

    def start(self) -> None:
        self._work = True

    def stop(self) -> None:
        self._work = False

        sleep(insignificant_read_every_ms)

        for wheel in self._wheels:
            wheel.stop()

    def work(self) -> None:
        while True:
            if self._work:
                self._read_sensors()
                self._update_wheel_speed()
            else:
                sleep(insignificant_read_every_ms)

    def _read_sensors(self) -> None:
        pass

    def _update_wheel_speed(self) -> None:
        pass


def register_button(robot: LineFollower, pin: str = INPUT_1) -> Thread:
    button = TouchSensor(pin)
    thread = Thread(target=initialize_button, args=(robot, button))
    thread.start()
    return thread


def initialize_button(robot: LineFollower, button: TouchSensor) -> None:
    sound = Sound()
    sound.set_volume(SOUND_VOLUME)
    sound.speak('Ready')

    while True:
        button.wait_for_bump(sleep_ms=insignificant_read_every_ms)
        sound.speak('Start')
        robot.start()

        button.wait_for_bump(sleep_ms=insignificant_read_every_ms)
        sound.speak('Stop')
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
