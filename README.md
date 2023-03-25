# Wstęp do Robotyki

Studenci:
```
Bartłomiej Krawczyk - 310774
Mateusz Brzozowski - 310608
```

# Mechanika

Robot z napędem różnicowym - dwa niezależnie napędzane koła stałe na jednej osi.

## Schemat
![Schemat](./img/schema.png)

## Podstawa matematyczna
- $v_p, v_l$ - prędkość liniowa prawego, lewego koła
- $\omega_p, \omega_l$ - prędkość kątowa prawego, lewego koła
- $v, \omega$ - prędkość liniowa i kątowa robota
- $R_C$ - chwilowy promień skrętu robota
- $d$ - rozstaw kół
- $r$ - promień koła

$$ v = \frac{v_l + v_p}{2} $$

$$ \omega = \frac{v_l - v_p}{d} $$

$$ R_C = \frac{v}{\omega} = \frac{d(v_l + v_p)}{2 (v_l - v_p)} $$

## Kod
<!-- base.py z opisami -->

Najpierw napisaliśmy podstawę do rozwijania kolejnych iteracji naszego kodu. Pozwoliło to nam przy kolejnych iteracjach jedynie kopiować podstawę i dowolnie ją modyfikować według potrzeb. Kod podstawy umieściliśmy w pliku [Baza](./base.py)

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
## Robot - iteracja I

1                                         | 2
------------------------------------------|------------------------------------------
![Fast Line Follower](./img/robot_i1.jpg) | ![Fast Line Follower](./img/robot_i2.jpg)
![Fast Line Follower](./img/robot_i3.jpg) | ![Fast Line Follower](./img/robot_i4.jpg)
![Fast Line Follower](./img/robot_i5.jpg) | ![Fast Line Follower](./img/robot_i6.jpg)
![Fast Line Follower](./img/robot_i7.jpg) | ![Fast Line Follower](./img/robot_i8.jpg)

## Robot - iteracja II
1                                         | 2
------------------------------------------|------------------------------------------
![Fast Line Follower](./img/robot_t1.jpg) | ![Fast Line Follower](./img/robot_t2.jpg)
![Fast Line Follower](./img/robot_t3.jpg) | ![Fast Line Follower](./img/robot_t4.jpg)
![Fast Line Follower](./img/robot_t5.jpg) | ![Fast Line Follower](./img/robot_t6.jpg)
![Fast Line Follower](./img/robot_t7.jpg) | ![Fast Line Follower](./img/robot_t8.jpg)

## Kod

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

<!-- Opisać, że testowaliśmy kilka iteracji rozwiązania -->
## Tor
<img
    src="./img/tournament.jpg" 
    width="50%" 
    style="display: block;margin-left: auto;margin-right: auto;"/>

## Wyniki

Team       | Round 1 | Round 2 | Round 3 | Round 4 | Round 5
-----------|---------|---------|---------|---------|--------
Parostatek | -       | 28.01   | -       | -       | 29.77



# Line Follower

## Kod

<!-- Zmniejszona prędkość względem zawodów, żeby wyrobić się na ostrych zakrętach -->

# Transporter

## Kod
<!-- Dodaj opis działania -->

```py

```


