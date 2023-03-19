# Wstęp do Robotyki

Studenci:
```
Bartłomiej Krawczyk - 310774
Mateusz Brzozowski - ??????
```

# Mechanika

## Podstawa matematyczna
<!-- Opis matematyczny -->

<!-- Zdjęcia + Schemat budowy -->
## Schemat
![Schema](./img/placeholder.png)

## Kod
<!-- base.py z opisami -->

Najpierw napisaliśmy podstawę do rozwijania kolejnych iteracji naszego kodu. Pozwoliło to nam przy kolejnych iteracjach jedynie kopiować podstawę i dowolnie ją modyfikować według potrzeb. Kod podstawy umieściliśmy w [Baza](./base.py)

Kod bazowy umożliwia nam:
- start programu
- zatrzymanie programu z upewnieniem się, że koła przestaną się poruszać
- głosowe potwierdzenie stanu (START, READY, STOP)
- wymagana jest jedynie implementacja jednej funkcji `iterate()`

```py
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
    pass


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
```

# Zawody

<!-- Warto wstawić zdjęcie toru - musimy to załatwić na następnych zajęciach. -->

## Robot
![Fast Line Follower](./img/placeholder.png)

## Kod

<!-- Opisać, że testowaliśmy kilka iteracji rozwiązania -->

### Kod "Naiwny"
<!-- Naiwny -->
<!-- Opisać, że "naiwny" nazywamy sterowanie jedynie na podstawie koloru - widzimy biały jedziemy - widzimy czarny cofamy dla odpowiedniej strony robota -->
<!-- Można zwrócić uwagę, że kolor badamy tylko raz na iterację -->

```py
FORWARD_SPEED = 30
TURN_SPEED = 40

SLEEP_SECONDS = 0.1

def iterate() -> None:
    colors = (
        left_sensor.color,
        right_sensor.color
    )
    if colors[LEFT] == colors[RIGHT]:
        move_tank.on(
            SpeedPercent(FORWARD_SPEED),
            SpeedPercent(FORWARD_SPEED)
        )
    elif colors[LEFT] != ColorSensor.COLOR_BLACK and colors[RIGHT] != ColorSensor.COLOR_BLACK:
        move_tank.on(
            SpeedPercent(FORWARD_SPEED),
            SpeedPercent(FORWARD_SPEED)
        )
    elif colors[LEFT] != ColorSensor.COLOR_WHITE and colors[RIGHT] == ColorSensor.COLOR_WHITE:
        move_tank.on(
            SpeedPercent(-FORWARD_SPEED - TURN_SPEED),
            SpeedPercent(FORWARD_SPEED + TURN_SPEED)
        )
    elif colors[LEFT] == ColorSensor.COLOR_WHITE and colors[RIGHT] != ColorSensor.COLOR_WHITE:
        move_tank.on(
            SpeedPercent(FORWARD_SPEED + TURN_SPEED),
            SpeedPercent(-FORWARD_SPEED - TURN_SPEED)
        )
    elif colors[LEFT] == ColorSensor.COLOR_NOCOLOR or colors[RIGHT] == ColorSensor.COLOR_NOCOLOR:
        move_tank.off()

    sleep(SLEEP_SECONDS)
```

### Kod bazujący na PID
<!-- PID -->

```py

```

<!-- Wpływ parametrów opisany -->

P | I | D | ZMIERZONY CZAS
--|---|---|---------------
a | b | c | -

# Line Follower

## Kod

<!-- Zmniejszona prędkość względem zawodów, żeby wyrobić się na ostrych zakrętach -->

# Tragarz

## Kod
<!-- Dodaj opis działania -->

```py

```


