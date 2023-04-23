# Zadania

Na pierwszych zajęciach prowadzący przekazał nam instrukcję z zadaniami jakie mieliśmy wykonać w trakcie trwania laboratoriów, następnie szczegółowo wytłumaczył nam na czym polegają poszczególne zadania.

## Zadanie 1 - Podążanie wzdłuż linii (Linefollower)

Zadaniem robota jest przejechanie całej trasy po wyznaczonej linii.

![Przykładowa trasa I](./img/trasa1.jpg){width=50%}\ ![Przykładowa trasa II](./img/trasa2.jpg){width=50%}

\begin{figure}[!h]
\caption{Przykładowa trasa do podążania za wyznaczoną linią}
\end{figure}

## Zadanie 2 - Transporter

Zadaniem robota jest przetransportowanie obiektów z punktów bazowych do punktów docelowych.
Punkt bazowy i punkt docelowy oznaczone są przez kolorowe elementy planszy. Rozwidlenie do opowiedniego koloru jest zaznaczone na czarnej linii trasy.

![Przykładowa plansza do zadania Transporter](./img/WR-kolor.jpg){width=75%}

# Założenia

Trasa do zadania pierwszego jest czarną linią na białym tle. Linia składa się nie tylko z prostych odcinków, lecz na drodze mogą znajdować się różnego rodzaju trudne zakręty, skrzyżowania do pokonania, takie jak np. ostre zakręty, zaokrąglone zakaty, skrzyżowania, zakrzywione linie.


\begin{figure}
\centering
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/line.jpg}
  \captionof{figure}{Prosta linia}
  \label{fig:test1}
\end{minipage}%
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/sharp_turn.jpg}
  \captionof{figure}{Ostry zakręt}
  \label{fig:test2}
\end{minipage}
\end{figure}

\begin{figure}
\centering
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/round_turn.jpg}
  \captionof{figure}{Zaokrąglony zakręt}
  \label{fig:test1}
\end{minipage}%
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/cross.jpg}
  \captionof{figure}{Skrzyżowanie}
  \label{fig:test2}
\end{minipage}
\end{figure}


![Zakrzywiona linia](./img/sharp_line.jpg){width=10%}

W ramach drugiego zadania trasa dodatkowo składa się z skrzyżowań odpowiednia oznaczonych wybranym kolorem. Kolory mogą się powtarzać, dlatego należy zapamiętywać stan robota. Trasa może dodatkowo zawierać np. kilka czerwonych skrzyżowań, zielonego skrzyżowania, czerwonej platformy, zielonej platformy z dłuższym dojazdem.

\begin{figure}
\centering
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/red_turn.jpg}
  \captionof{figure}{Czerwone skrzyżowanie}
  \label{fig:test1}
\end{minipage}%
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/green_turn.jpg}
  \captionof{figure}{Zielone skrzyżowanie}
  \label{fig:test2}
\end{minipage}
\end{figure}

\begin{figure}
\centering
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/red_platform.jpg}
  \captionof{figure}{Czerwona platforma}
  \label{fig:test1}
\end{minipage}%
\begin{minipage}{.5\textwidth}
  \centering
  \includegraphics[width=.4\linewidth]{./img/green_platform.jpg}
  \captionof{figure}{Zielona platforma}
  \label{fig:test2}
\end{minipage}
\end{figure}

# Przygotowanie do pracy

Przed przystąpieniem do rozwiązywania zadań otrzymaliśmy od prowadzącego laboratoria części robota `LEGO Mindstorms Ev3`, a także klocki `LEGO`, które posłużyły nam do zbudowania naszego robota.

![Otrzymane elementy robota LEGO Mindstorms Ev3](./img/elements.jpg){width=75%}

Poszczególne elementy posiadają różne funkcjonalności, które po złożeniu w całość pomogły nam rozwiązać zadania.

Do zadania pierwszego wykorzystaliśmy następujące elementy robota takie jak:

: Otrzymane elementy robota - zadanie 1 \label{tab:elementsone}

| Element                    | Zastosowanie                                                                       | Zdjęcie                                  |
|----------------------------|------------------------------------------------------------------------------------|------------------------------------------|
| główna jednostka sterująca | Uruchamia program, odbiera i nadaje sygnały do poszczególnych czujników i silników | ![](./img/core.jpg){width=25%}           |
| 2 x silnik napędowy do kół | Do silników były przymocowane koła, które umożliwiły poruszanie sie robota         | ![](./img/move_engine.jpg){width=25%}    |
| 2 x czujnik światła        | Wykrywanie lini i kolorów jakie znajdowały sie pod robotem                         | ![](./img/color_detector.jpg){width=25%} |
| przycisk                   | Uruchamianie i zatrzymywanie robota                                                | ![](./img/button.jpg){width=25%}         |

Posłużyły nam one do wykrywania linii i poruszania się wzdłuż niej. Jednakże w przypadku rozwiązywania kolejnego zadania, przedstawione elementy okazały się niewystarczające, ponieważ oprócz śledzenia musieliśmy jeszcze wykrywać obiekt, podnosić go i opuszczać. Dlatego dodatkowo w przypadku rozwiązywania zadania 2 dołożyliśmy następujące elementy:

: Otrzymane elementy robota - zadanie 2 \label{tab:elementstwo}

| Element            | Zastosowanie                                       | Zdjęcie                                     |
|--------------------|----------------------------------------------------|---------------------------------------------|
| serwomechanizm     | Podnoszenie i opuszczanie obiektu                  | ![](./img/servo.jpg){width=25%}             |
| czujnik odległości | Wykrywanie w jakiej odległości znajduje się obiekt | ![](./img/distance_detector.jpg){width=25%} |

# Realizacja

Początek pracy poświęciliśmy na zapoznanie się z wykładami udostępnionymi w ramach wykładów z przedmiotu Wstęp Do Robotyki. Dzięki temu zgłębiliśmy matematyczne podstawy tego w jaki sposób może poruszać się pojazd kołowy.

## Mechanika

Robot z napędem różnicowym - dwa niezależnie napędzane koła stałe na jednej osi.

W celu zmiany położenia modyfikowaliśmy prędkości kół. Założyliśmy jedną prędkość podstawową do przodu oraz dodatkowo modyfikowaliśmy skręt odpowiednio modyfikując składowe prędkości poszczególnych kół.

Prędkość naszego robota do przodu wynikała ze średniej prędkości obu kół, a prędkość obrotu zależała od różnicy między prędkościami kół.

## Schemat

![Schemat](./img/schema.png){width=75%}

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

## Rozwiązanie bazujące na PID

#### Wpływ parametrów PID

- **Parametr P**
    - parametr brany z największą wagą
    - oznaczał chwilową różnicę w poziomie odbijanego światła odbieranego przez czujniki
- **Parametr I**
    - parametr brany z najmniejszą wagą (ponieważ `integral` był bardzo dużą liczbą w porównaniu do `error` oraz `derivative`)
    - `integral` przechowywał historię kilku ostatnich iteracji programu, przez co powodował, że jak wyjechaliśmy jedynie w niewielkim stopniu to skręt był niewielki, jednak gdy przez dłuższy czas czujniki wykrywały linię to poziom skrętu zwiększał się
- **Parametr D**
    - parametr wynikał z chwilowej zmiany między poziomem lewego i prawego czujnika
    - parametr miał największy wpływ w przypadku ostrych skrętów
    - parametr liczył się jedynie przy zmianie między ostatnimi błędami

## Dobieranie parametrów

Parametry PID, które zastosowaliśmy w naszym robocie, zostały dobrane metodą inżynierską. Zastosowaliśmy podejście iteracyjne, w którym kolejne wartości parametrów były ustalane na podstawie wyników testów oraz obserwacji zachowania robota.

W zależności od rodzaju zadania, dla którego był przeznaczony robot, dobieraliśmy parametry PID w inny sposób. Na przykład, podczas zawodów głównie skupialiśmy się na zwiększaniu prędkości przy okazji odpowiednio modyfikując parametr D, ponieważ tor nie posiadał ostrych zakrętów. Zwiększaliśmy również parametr I, aby nasz robot na odcinkach prostych mógł osiągnąć jak największą prędkość. W przypadku parametrów D i I staraliśmy się dobrać odpowiednią wartość na podstawie doświadczenia.

W zadaniu Line Follower skupiliśmy się na dostosowaniu wartości parametrów P i D, ponieważ było tam dużo ostrych zakrętów. Zaczęliśmy od wartości, które sprawdziły się podczas zawodów, a następnie stosowaliśmy iteracyjną metodę doboru wartości parametrów, aż do osiągnięcia idealnych wartości, które okazały się takie same jak wartości początkowe. W tym przypadku jedyną zmianą, jaką wprowadziliśmy, było zmniejszenie prędkości ruchu robota.

W ostatnim zadaniu pozostawiliśmy parametry prawie takie same jak w poprzednim zadaniu, jednakże zmniejszyliśmy prędkość ruchu robota. W przypadku tego zadania dodatkowo musieliśmy wyznaczyć ilość obrotów kół jakie musi wykonać nasz robot aby wykonać pełen obrót o 360 stopni, tak aby w prosty sposób dokonywać obrotów w prawo/lewo, a także zawracania.

## Wyniki

: Wyniki zawodów \label{tab:statsone}

Team       | Round 1 | Round 2 | Round 3 | Round 4 | Round 5
-----------|---------|---------|---------|---------|--------
Parostatek | -       | 28.01   | -       | -       | 29.77

### Wnioski

- najcięższe było dobranie parametrów PID, tak aby robot jeździł z zadowalającą prędkością

## Line Follower

### Parametry

Zmniejszona prędkość względem zawodów, żeby wyrobić się na ostrych zakrętach:
[Podstawowe PID](./line_follower/pid_basic.py)

```{.python caption="Zmodyfikowane parametry - zadanie śledzenia lini" #lst:singleton}
MIN_FORWARD_SPEED = 10
MAX_FORWARD_SPEED = 20

FORWARD_SPEED_CORRECTION = (
    (MAX_FORWARD_SPEED - MIN_FORWARD_SPEED) / MAX_FORWARD_SPEED
)

CONSTANT_P = 4.0
CONSTANT_I = 0.01
CONSTANT_D = 4.0

HISTORY_LOSS = 0.5

AMPLIFIER = 0.25
```

## Transporter

Aby przetransportować obiekt z jednego miejsca na drugi musieliśmy na początku przeanalizować wszystkie możliwe stany, jakie mogą wystąpić w tracie zadania. Tak więc, przygotowaliśmy schemat stanowy, który przedstawia to jak ma zachowywać się w danym momencie.

```mermaid
stateDiagram-v2
    1: Jazda wzdłuż czarnej lini
    2: Skręt w prawo
    3: Skręt w lewo
    4: Jazda wzdłuż czarnej lini
    5: Podniesienie obiektu, obrót o 180 stopni i jazda wzdłuż czarnej lini
    6: Skręt w lewo i jazda wzdłuż czarnej lini
    7: Skręt w prawo
    8: Skręt w lewo
    9: Jazda wzdłuż czarnej lini
    10: Upuszczenie obiektu, wycofanie i zagranie melodii
    [*] --> 1

    1 --> 2: Znalezienie zielonej lini z prawej strony
    1 --> 3: Znalezienie zielonej lini z lewej strony
    2 --> 4
    3 --> 4
    4 --> 5: Wykrycie obiektu przed pojazdem
    5 --> 6: Wykrycie prostopadłej czarnej lini
    6 --> 7: Znalezienie czerwonej lini z prawej strony
    6 --> 8: Znalezienie czerwonej lini z lewej strony
    7 --> 9
    8 --> 9
    9 --> 10: Wykrycie czerwonego kwadratu
    10 --> [*]
```

## Tor

Do każdego rodzaju zadania z jakim musiał zmierzyć się nasz robot, przygotowywany był odpowiedni tor.

| Rodzaj zadania | Zdjęcie toru |
|-|-|
| Zawody | ![Tor na zawody](./img/tournament.jpg){width=50%}
| Line Follower | ![Tor - podążanie za linią](./img/line_follower.jpg){width=30%}
| Transporter | ![Trasa dla transportera](./img/transporter_road.jpg){width=50%}


\newpage

# Budowa robota

## Zawody

Wykorzystując otrzymane przez prowadzącego laboratoria elementy robota, a także udostępnioną pokaźną ilość kloców lego przystąpiliśmy do budowy robota.

### Robot - iteracja I

Budowę naszego robota rozpoczęliśmy od zamontowania kół, dwóch z przodu robota, oraz jednego samonastawnego z tyłu. Posłużyła nam do tego dolna podstawa, zamontowana do robota, zwiększająca jego stabilność, a także umożliwiająca przemontowanie czujników światła, które chcieliśmy aby znalazły się na wysokości przednich kół.

![](./img/robot_i1.jpg){width=50%}\ ![](./img/robot_i2.jpg){width=50%}
![](./img/robot_i3.jpg){width=50%}\ ![](./img/robot_i4.jpg){width=50%}

\begin{figure}[!h]
\caption{Pierwsza iteracja robota - z kołem samonastawnym}
\end{figure}

\newpage

![](./img/robot_i5.jpg){width=50%}\ ![](./img/robot_i6.jpg){width=50%}
![](./img/robot_i7.jpg){width=50%}\ ![](./img/robot_i8.jpg){width=50%}

\begin{figure}[!h]
\caption{Pierwsza iteracja robota - z kołem samonastawnym}
\end{figure}

\newpage

### Robot - iteracja II

W celu uzyskania lepszych czasów w czasie trwania zawodów zamieniliśmy koło samonastawne na kulę, która spowodowała zmniejszenie tarcia o powierzchnię w rezultacie, zwiększyła szybkość poruszania się robota.

![Fast Line Follower](./img/robot_t1.jpg){width=50%}\ ![Fast Line Follower](./img/robot_t2.jpg){width=50%}
![Fast Line Follower](./img/robot_t3.jpg){width=50%}\ ![Fast Line Follower](./img/robot_t4.jpg){width=50%}

\begin{figure}[!h]
\caption{Druga iteracja robota - z kulą zamiast koła wspierającego}
\end{figure}

\newpage

![Fast Line Follower](./img/robot_t5.jpg){width=50%}\ ![Fast Line Follower](./img/robot_t6.jpg){width=50%}
![Fast Line Follower](./img/robot_t7.jpg){width=50%}\ ![Fast Line Follower](./img/robot_t8.jpg){width=50%}

\begin{figure}[!h]
\caption{Druga iteracja robota - z kulą zamiast koła wspierającego}
\end{figure}

\newpage

## Line Follower

Do zaliczenia pierwszego zadania, polegającego na śledzeniu linii, wykorzystaliśmy II iterację robota zbudowanego w czasie trwania zawodów.

## Transporter

W tym etapie przebudowaliśmy trochę nasz robot w taki sposób, aby mógł wykrywać i przewozić zbudowany przez nas przedmiot. Dlatego też, czujnik odległości, aby poprawnie rozpoznawał obliczał odległość obiektów znajdujących się przed robotem, musiał być zamontowany przed czujnikami światła, dodatkowo musiał znaleźć się na tyle nisko, aby nie utrudniał pracy wysięgnika. Tak więc przemontowaliśmy go do dolnej podstawy robota, pomiędzy czujnikami światła, lekko wysuniętym do przodu. Podnośnik zamontowaliśmy u góry, na wyciągniętych ramionach, tak aby znajdował sie nad czujnikiem odległości, a jako ramiona do podnoszenia wybraliśmy prostopadle zamontowane zakrzywione klocki, tak aby w łatwy sposób unieść obiekt znajdujący sie przed robotem.

![](./img/robot_tr1.jpg){width=50%} \ ![](./img/robot_tr2.jpg){width=50%}

![](./img/robot_tr3.jpg){width=50%} \ ![](./img/robot_tr4.jpg){width=50%}

\begin{figure}[!h]
\caption{Trzecia iteracja robota - wspierająca detekcję i przenoszenie przedmiotów}
\end{figure}

## Działający robot

[LINK DO NAGRANIA NA YOUTUBE](https://youtu.be/3knkUJOpiRk)


# Implementacja

## Kod bazowy
<!-- base.py z opisami -->

Najpierw napisaliśmy podstawę do rozwijania kolejnych iteracji naszego kodu. Pozwoliło to nam przy kolejnych iteracjach jedynie kopiować podstawę i dowolnie ją modyfikować według potrzeb. Kod podstawy umieściliśmy w pliku [Baza](./base.py)

Kod bazowy umożliwia nam:
- start programu
- zatrzymanie programu z upewnieniem się, że koła przestaną się poruszać
- głosowe potwierdzenie stanu (START, READY, STOP)
- wymagana jest jedynie implementacja jednej funkcji `iterate()`

```{.python caption="Bazowy kod programu" #lst:singleton}
def speak(message: str) -> None:
    sound.speak(message)
    print(message)


def work() -> None:
    while True:
        if button.is_pressed:
            handle_button_pressed()
        else:
            try:
                iterate()
            except Exception as e:
                print(e)


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

## Kod Line Follower'a

W ramach tego zadania rozbudowaliśmy bazowy kod, o funkcjonalność robota, tak aby ten mógł rozpoznawać linię i podążać za nią. Na zajęcia przygotowaliśmy dwie wersje kodu. `Kod "Nawiny"`, bezpośrednio reagujący na to co odbierają czujniki oraz `Kod bazujący na PID`, który ostatecznie został wykorzystany do zaliczenia zadania.

### Kod "Naiwny"

Na samym początku założyliśmy naiwny sposób śledzenia lini - kod dostępny jest w pliku [Naiwny](./trials/naive.py)

Określeniem "naiwny" nazywamy sterowanie jedynie na podstawie koloru - widzimy biały jedziemy - widzimy czarny cofamy dla odpowiedniej strony robota.

```{.python caption="Śledzenie lini - kod naiwny" #lst:singleton}
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

Przygotowaliśmy kilka iteracji kodu naiwnego, jednak nie sprawdzały się w takim stopniu, jaki chcieliśmy:

- [Naiwny](./trials/naive_atrocity.py)
- [Naiwny](./trials/naive_trying_to_be_clever.py)
- [Naiwny](./trials/naive_pid.py)

### Kod bazujący na PID

Przygotowaliśmy także kilka wersji kodu, które działają na bazie PID, opartej o poziom odbitego światła:

- [PID](./trials/move_tank.py)
- [PID](./trials/pid_discrete_forward_speed.py)
- [PID](./trials/pid_trying_to_be_clever.py)

Ostatecznie po dopracowaniu kodu wpadliśmy na pomysł, żeby manipulować prędkość na prostych w zależności od wyliczonej prędkości skrętu. Na odcinkach prostych, gdy prędkość skrętu była bliska 0 jechaliśmy z prędkością maksymalną - `100`, gdy prędkość skrętu wzrastała odpowiednio zmniejszaliśmy prędkość do przodu, tak do osiągnięcia minimalnej prędkości do przodu.

- [Najszybszy](./tournament/pid_tournament.py)

```{.python caption="Śledzenie lini - kod bazujący na PID" #lst:singleton}
MIN_FORWARD_SPEED = 30
MAX_FORWARD_SPEED = 100

FORWARD_SPEED_CORRECTION = (
    (MAX_FORWARD_SPEED - MIN_FORWARD_SPEED) / MAX_FORWARD_SPEED
)

CONSTANT_P = 4.0
CONSTANT_I = 0.01
CONSTANT_D = 4.0

HISTORY_LOSS = 0.5

AMPLIFIER = 0.1

def iterate(integral: float, last_error: int) -> Tuple[float, int]:
    error = left_sensor.reflected_light_intensity - \
        right_sensor.reflected_light_intensity

    integral = HISTORY_LOSS * integral + error
    derivative = error - last_error
    last_error = error

    turn_speed = CONSTANT_P * error + CONSTANT_I * integral + CONSTANT_D * derivative

    forward_speed = max(
        MIN_FORWARD_SPEED,
        MAX_FORWARD_SPEED - FORWARD_SPEED_CORRECTION * abs(turn_speed)
    )

    left_motor.on(forward_speed + AMPLIFIER * turn_speed)
    right_motor.on(forward_speed - AMPLIFIER * turn_speed)

    return integral, last_error
```

## Kod Transporter'a

W ramach ostatniego zadania rozbudowaliśmy funkcjonalność kodu z poprzedniego zadania `Kod bazujący na PID`.

Zdefniowaliśmy stany:
```{.python caption="Stany osiągane przez transporter" #lst:singleton}
FOLLOW_LINE_UNTIL_PICK_UP = 0
FOLLOW_LINE_UNTIL_DETECTED_OBJECT = 1
FOLLOW_LINE_UNTIL_TWO_LINES_DETECTED = 2
FOLLOW_LINE_UNTIL_DROP_DOWN = 3
FOLLOW_LINE_UNTIL_TWO_DROP_DOWN_COLORS_DETECTED = 4
STATE_STOP = 5
```

Zaktualizowaliśmy główną pętlę:
```{.python caption="Zmodyfikowana pętla bazowa programu" #lst:singleton}
def work() -> None:
    integral = 0.0
    last_error = 0

    state = FOLLOW_LINE_UNTIL_PICK_UP

    while True:
        if button.is_pressed:
            handle_button_pressed()
            integral = 0.0
            last_error = 0
            state = FOLLOW_LINE_UNTIL_PICK_UP
        else:
            state, integral, last_error = iteration(
                state, integral, last_error
            )
```

W pętli na podstawie stanu wołaliśmy odpowiednią funkcję obsługi:
```{.python caption="Decyzję, jakiej funkcji obsługi użyć podejmowaliśmy na podstawie stanu" #lst:singleton}
ITERATION_FUNCTION = {
    FOLLOW_LINE_UNTIL_PICK_UP: follow_line_until_pick_up,
    FOLLOW_LINE_UNTIL_DETECTED_OBJECT: follow_line_until_detected_object,
    FOLLOW_LINE_UNTIL_TWO_LINES_DETECTED: follow_line_until_two_lines_detected,
    FOLLOW_LINE_UNTIL_DROP_DOWN: follow_line_until_drop_down,
    FOLLOW_LINE_UNTIL_TWO_DROP_DOWN_COLORS_DETECTED: follow_line_until_two_drop_down_colors_detected,
}


def iteration(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    function = ITERATION_FUNCTION.get(state, stop_robot)
    state, integral, last_error = function(state, integral, last_error)
    return state, integral, last_error
```

Dla każdego stanu zdefniowaliśmy obsługę:

- Śledzenie lini z wykorzystaniem algorytmu korzystającego z PID, dopóki nie napotkamy koloru z którego powinniśmy podnieść przedmiot
- Gdy odpowiednio na lewym lub prawym czujniku wykryjemy dany kolor to zaczynamy obracać się w tym kierunku
- Obrót o 90 stopni jest wyliczony i zawsze wykonywane jest tyle samo obrotów kół - zakładamy brak poślizgu
- Następnie aktualizowany jest stan - średzenie lini dopóki nie napotkamy obiektu

```{.python caption="Obsługa śledzenia linii do momentu napotkania koloru z którego należy podnieść przedmiot" #lst:singleton}
def follow_line_until_pick_up(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    colors = detect_colors()
    if colors[LEFT] == COLORS[PICK_UP]:
        turn_left()
        state = FOLLOW_LINE_UNTIL_DETECTED_OBJECT
    elif colors[RIGHT] == COLORS[PICK_UP]:
        turn_right()
        state = FOLLOW_LINE_UNTIL_DETECTED_OBJECT
    else:
        integral, last_error = follow_line(integral, last_error)

    return state, integral, last_error
```

- Śledzenie lini z wykorzystaniem PID dopóki czujnik odległości nie wykryje przedmiotu w odległości 1 od przodu robota
- Gdy odległość jest wystarczająco bliska to podnosimy przedmiot, obracamy się o 180 stopni (wyliczona ilość obrotów kół) i przechodzimy do następnego stanu
```{.python caption="Obsługa śledzenia lini do momentu wykrycia przedmiotu przed robotem" #lst:singleton}
def follow_line_until_detected_object(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    detected_distance = distance()
    if detected_distance < 2:
        pick_up()
        turn_around()
        state = FOLLOW_LINE_UNTIL_TWO_LINES_DETECTED
    else:
        integral, last_error = follow_line(integral, last_error)
    return state, integral, last_error
```

- Po podniesieniu przedmiotu śledziliśmy linię dopóki nie napotkamy na obu czujnikach koloru - koloru czarnego - oznaczało, to że dojechaliśmy do skrzyżowania
- na skrzyżowaniu skręcaliśmy w prawo, a następnie przechodziliśmy do kolejnego stanu
```{.python caption="Obsługa śledzenia lini do momentu wykrycia skrzyżowania" #lst:singleton}
def follow_line_until_two_lines_detected(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    colors = detect_colors()
    if colors[LEFT] == ColorSensor.COLOR_BLACK and colors[RIGHT] == ColorSensor.COLOR_BLACK:
        turn_right()
        state = FOLLOW_LINE_UNTIL_DROP_DOWN
    else:
        integral, last_error = follow_line(integral, last_error)

    return state, integral, last_error
```

- Podobnie jak w stanie pierwszym śledziliśmy linię dopóki na jednym z czujników nie wykryjemy koloru na który należy odłożyć przedmiot
- Gdy wykryjemy kolor to skręcamy w odpowiednią stronę i przechodzimy do następnego stanu
```{.python caption="Obsługa śledzenia lini do momentu napotkania koloru na który należy odłożyć przedmiot" #lst:singleton}
def follow_line_until_drop_down(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    colors = detect_colors()
    if colors[LEFT] == COLORS[DROP_DOWN]:
        turn_left()
        state = FOLLOW_LINE_UNTIL_TWO_DROP_DOWN_COLORS_DETECTED
    elif colors[RIGHT] == COLORS[DROP_DOWN]:
        turn_right()
        state = FOLLOW_LINE_UNTIL_TWO_DROP_DOWN_COLORS_DETECTED
    else:
        integral, last_error = follow_line(integral, last_error)

    return state, integral, last_error
```

- Na sam koniec pozostało śledzenie lini dopóki nie wykryjemy na obu czujnikach koloru - koloru docelowego
- Gdy wykryjemy ten kolor to odkładamy przedmiot, puszczamy muzykę i obracamy się w miejscu, po czym zatrzumujemy robota
```{.python caption="Obsługa śledzenia lini do momentu wykrycia kwadratu na który należy odłożyć przedmiot" #lst:singleton}
def follow_line_until_two_drop_down_colors_detected(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    colors = detect_colors()
    if colors[LEFT] == COLORS[DROP_DOWN] and colors[RIGHT] == COLORS[DROP_DOWN]:
        drop_down()
        sound.play_song(WINNING_SONG)
        turn_around()
        state = STATE_STOP
    else:
        integral, last_error = follow_line(integral, last_error)

    return state, integral, last_error

WINNING_SONG = (
    ('D4', 'e3'),  # intro anacrouse
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),   # meas 1
    ('D5', 'h'),
    ('C5', 'e3'),  # meas 2
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),  # meas 3
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),  # meas 4
    ('B4', 'e3'),
    ('C5', 'e3'),
    ('A4', 'h.'),
)
```

- W ostatnim stanie resetujemy ustawienie robota i oczekujemy na przycisk, aby robot mógł wystartować ponownie
```{.python caption="Ostatni stan - zatrzymanie robota i oczekiwanie na wciśnięcie przycisku" #lst:singleton}
def stop_robot(state: int, integral: float, last_error: int) -> Tuple[int, float, int]:
    handle_button_pressed()
    state = FOLLOW_LINE_UNTIL_PICK_UP
    integral = 0.0
    last_error = 0
    return state, integral, last_error
```

Funkcje pomocnicze:

Wykrywanie kolorów
- mieliśmy problem z kolorem wykrywanym przez migające na zmianę czujniki
- aby ujednolicić pomiary najpierw zmienialiśmy tryb wykrywania czujników, a następnie dopiero wykrywaliśmy kolor
```{.python caption="Funkcja pomocnicza - wykrywanie koloru" #lst:singleton}
def detect_colors() -> Tuple[int, int]:
    ensure_mode(ColorSensor.MODE_COL_COLOR)
    return (
        left_sensor.color,
        right_sensor.color
    )

def ensure_mode(color: str) -> None:
    left_sensor.mode = color
    right_sensor.mode = color
    sleep(TIME_PER_MODE_CHANGE)
```

Stała ilość rotacji w miejscu:
- ponieważ czujniki są minimalnie przesunięte do przodu względem osi kół, to przed obrotem jedziemy minimalnie do przodu, aby po obrocie robot skończył z czujnikami wokół lini
- podobnie po skończonym obrocie jasność kolorów na które wjeżdżamy nie zawsze pozwalała nam na dobre rozróżnianie tych kolorów od koloru białego za pomocą czujników odbijających światło czerwone - więc rozwiązaliśmy to przejechaniem przez ten kolor po prostej i dopiero gdy dojechaliśmy do koloru czarnego załączało się dalsze śledzenie lini
```{.python caption="Funkcje pomocnicze - obrót" #lst:singleton}
ROTATIONS_PER_FULL_ROTATION = 3.15

def turn(full_roations: float, speed: int) -> None:
    rotations = ROTATIONS_PER_FULL_ROTATION * full_roations
    forward_for_rotations(0.1)
    left_motor.on_for_rotations(
        speed,
        rotations,
        block=False
    )
    right_motor.on_for_rotations(
        - speed,
        rotations,
    )
    forward_for_rotations(0.3)


def forward_for_rotations(rotations: float) -> None:
    left_motor.on_for_rotations(
        MIN_FORWARD_SPEED,
        rotations,
        block=False
    )
    right_motor.on_for_rotations(
        MIN_FORWARD_SPEED,
        rotations
    )


def turn_around() -> None:
    turn(0.5, MAX_FORWARD_SPEED)


def turn_left() -> None:
    turn(0.25, -MAX_FORWARD_SPEED)


def turn_right() -> None:
    turn(0.25, MAX_FORWARD_SPEED)
```