# Übung 2
**Schreibe ein Programm dass dem User eine Reihe von Rechenaufgaben lösen lässt.**

Am Ende sollte das ganze so aussehen:
```shell
Was ist 3 + 6?

> 7

Das ist leider falsch.
Die richtige Antwort ist 9

Was ist 3 + 6?

> 9

Das ist richtig.
```

# Erweiterung 1
Erweitere dein Programm und speichere die Zahlen der Summanden und das Ergebnis in Variablen.

# Erweiterung 2
Erweitere dein Programm und sorge dafür, dass die Summanden zufällig ausgewählt werden und berechne das Ergebnis in der Ergebnis-Variablen.

# Erweiterung 3
Erweitere dein Programm und führe einen "Streak" ein. Der Benutzer bekommt so lange neue, zufällige Aufgaben, bis er 3 mal die Aufgaben korrekt gelöst hat.

Das Ergebnis soll so aussehen:
```shell
Was ergibt 3 + 10?

> 13

Das ist richtig!  Streak: 1
Was ergibt 1 + 9?

> 10

Das ist richtig!  Streak: 2
Was ergibt 2 + 2?

> 3

Das ist leider falsch
Die richtige Antwort ist 4
Was ergibt 4 + 5?

> 9

Das ist richtig!  Streak: 3
Super! Du hast 3 Aufgaben richtig gelöst :D
```

# Erweiterung 4
Erweitere dein Programm, dass der Nutzer nur dann gewonnen hat, wenn er 3 Aufgaben **hintereinander** korrekt gelöst hat.

Das Ergebnis soll so aussehen:
```shell
Was ergibt 3 + 10?

> 13

Das ist richtig!  Streak: 1
Was ergibt 1 + 9?

> 10

Das ist richtig!  Streak: 2
Was ergibt 2 + 2?

> 3

Das ist leider falsch
Die richtige Antwort ist 4
Was ergibt 3 + 10?

> 13

Das ist richtig!  Streak: 1
Was ergibt 1 + 9?

> 10

Das ist richtig!  Streak: 2
Was ergibt 2 + 2?

> 4

Was ergibt 4 + 5?

> 9

Das ist richtig!  Streak: 3
Super! Du hast 3 Aufgaben hintereinander richtig gelöst :D
```

# Erweiterung 6
Erweitere dein Programm, dass die Anzahl der Versuche in einer Variablen steht.

# Erweiterung 7
Erweitere dein Programm um eine Fehlerprüfung. Wenn der Nutzer keine Zahl eingibt, dann soll folgende Fehlermeldung angezeigt werden und das Programm mit einer neuen Aufgabe fortfahren.

```shell
Bitte gib eine Zahl ein!
```
