# Aufgabe: CCD

Bearbeiter: Kevin Skyba

Zur Bearbeitung der Aufgabe wird ein kleines konsolenbasiertes [QANGO](https://www.yucata.de/de/Rules/QANGO) Spiel in Python entwickelt. Die Implementierung wurde nicht bis zur Ausführbarkeit getrieben, sondern sollte eher das gesamte Spiel als Library abbilden, sodass durch einfache Nutzung der Klasse `Game` ein beliebiges Frontend vorgesetzt werden kann.

## Principles

Ich habe mich für folgende Prinzipien entschieden:

* Keep it simple, stupid (KISS)
* Avoid Early Optimizations
* Single Level of Abstraction (SLA)
* Use assertions! Pre / Post Conditions
* Separation of Concerns (SoC)
* Unused Code

## Analyse

Der Code kann unter [diesem Link](code/qango/) angesehen werden. Im folgendem nehme ich jeweils zu einem der oben genannten Prinzipien beispielhaft in Form einer Code-Stelle Stellung.

### Keep it simple, stupid (KISS)

[Zur Auswertung der Siegbedingungen](code/qango/win_conditions.py) hätte man für alle möglichen Fälle einen allgemein gültigen Algorithmus entwickeln können. In diesem Spiel sind die Siegbedingungen aber sehr einfach und übersichtlich, weshalb durch diese Implementierung sowohl Performance als auch Verständlichkeit sichergestellt wurden. Für die "blockweisen" und vertikalen sowie horizontalen Siegbedingungen wurden dann durch einfache Iteration der Möglichkeiten ermittelt.

### Avoid Early Optimizations

Auch hier nehme ich wieder die [Siegbedingungen](code/qango/win_conditions.py) als Beispiel.

### Single Level of Abstraction (SLA)

Es wurde darauf geachtet, dass der Code für den Nutzer nach vorne hin vollständig abstrahiert ist. Der Nutzer muss lediglich die Klasse `Game` in [game.py](code/qango/game.py) nutzen, welche alle Mechaniken für ihn abstrahieren. Diese Klasse arbeitet dann intern mit der Implementierung von `win_conditions.py`(code/qango/win_conditions.py) sowie von [game_state.py](code/qango/game_state.py), in welcher die gesamte Logik des Spiels mit eingebauter "Historie-Funktion" mit der Möglichkeit der späteren oder parallelen Analyse von Spielzügen implementiert ist.

### Use assertions! Pre / Post Conditions

Es wurde darauf geachtet, dass alle Funktionen keine Crashes erzeugen können. An einer Stelle jedoch gibt es eine Pre-Condition, welche unter [game_state.py](code/qango/game_state.py) in Zeile 68 zu finden ist.

### Separation of Concerns (SoC)

Jede Klasse hat eine für sie dedizierte Aufgabem welche nur sie übernimmt. [game.py](code/qango/game.py) ist das Herz welches alle Klassen miteinander verbindet und nach außen hin ein abstrahiertes Interface anbietet. [game_state.py](code/qango/game_state.py) implementiert die Logik des Spiels. Unter [token.py](code/qango/token.py) sind die verwendeten Token im Spiel abstrahiert, welche für das Rendering verwendet werden und unter [win_conditions.py](code/qango/win_conditions.py) ist die einzige Stelle an der entschieden wird, ob ein Spiel für einen der Spieler gewonnen ist.

Außerdem wurde eine gewisse Erweiterbarkeit angedacht. Die Logik der Gewinnauswertung kann komplett über [win_conditions.py](code/qango/win_conditions.py) ausgetauscht werden, und auch nur hier!

### Unused Code

Jede einzelne Code-Zeile wird verwendet und es gibt keinen "toten" oder "unsued" Code.