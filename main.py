#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from typing import List

LEFT = 0
RIGHT = 1

TURN_FORWARD_SPEED = 8
FORWARD_SPEED = 20
MAX_TURN_SPEED = 40

ERROR_MULTIPLIER = 8.0
INTEGRAL_MULTIPLIER = 0.9
DERIVATIVE_MULTIPLIER = 0.003

HISTORY_LOSS_SPEED = 0.5

SOUND_VOLUME = 100
INSIGNIFICANT_READ_FREQUENCY_HZ = 4

insignificant_read_every_ms = int(INSIGNIFICANT_READ_FREQUENCY_HZ / 1000)


class LineFollower:

    def __init__(
        self,
        sound: Sound,
        button: TouchSensor,
        wheel_pins: List[str] = [OUTPUT_A, OUTPUT_B],
        color_sensor_pins: List[str] = [INPUT_1, INPUT_2]
    ) -> None:

        self._integral = 0.0
        self._last_error = 0.0
        self._derivative = 0.0
        self._wheels = [
            LargeMotor(pin) for pin in wheel_pins
        ]
        self._color_sensors = [
            ColorSensor(pin) for pin in color_sensor_pins
        ]
        self._follow_line = False
        self._forward_speed = FORWARD_SPEED
        self._turn_speed = [0, 0]
        self._button = button
        self._sound = sound

    def start(self) -> None:
        self._calibrate = [
            sensor.reflected_light_intensity for sensor in self._color_sensors]

    def stop(self) -> None:
        for wheel in self._wheels:
            wheel.stop()

    def work(self) -> None:
        while True:
            self._read_sensors()
            self._update_wheel_speed()

            if self._button.is_pressed:
                self.stop()
                self._sound.speak('STOP')
                self._button.wait_for_released()
                self._button.wait_for_bump()
                self._sound.speak('START')

    def _read_sensors(self) -> None:
        left_read = self._color_sensors[LEFT].reflected_light_intensity - \
            self._calibrate[LEFT]
        right_read = self._color_sensors[RIGHT].reflected_light_intensity - \
            self._calibrate[RIGHT]
        print('Left = ', left_read, ' Right = ', right_read)

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
        print('Error = ', self._error)
        print('Integral = ', self._integral)
        print('Derivative = ', self._derivative)
        print(self._turn_speed)
        for wheel, turn_speed in zip(self._wheels, self._turn_speed):
            turn = turn_speed // 10
            rounded = max(min(turn, MAX_TURN_SPEED), -MAX_TURN_SPEED)

            if turn != rounded:
                wheel.on(TURN_FORWARD_SPEED + rounded)
            else:
                wheel.on(self._forward_speed + rounded)


def main() -> None:
    sound = Sound()
    button = TouchSensor(INPUT_3)
    robot = LineFollower(sound, button)
    robot.stop()

    sound.set_volume(SOUND_VOLUME)
    sound.speak('Ready')
    print('READY')

    button.wait_for_bump(sleep_ms=insignificant_read_every_ms)
    sound.speak('Start')
    print('START')

    robot.start()

    try:
        robot.work()
    except KeyboardInterrupt as e:
        robot.stop()
        raise e


if __name__ == '__main__':
    main()
