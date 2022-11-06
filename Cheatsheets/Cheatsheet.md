# Funktionen

| Befehl | Auf Deutsch | macht: |
| --- | --- | --- |
| print() | drucken | &quot;druckt&quot; den Inhalt der Klammern auf das Terminal aus |

### Beispiel
 ```python 
 print("Hallo Welt!")  
 ``` 
### Ausabe
```shell
> Hallo Welt
``` 

| Befehl | Auf Deutsch | macht: |
| --- | --- | --- |
| input() | eingeben | gibt eine Eingabe, die über das Terminal<br>eingegeben wird zurück<br>druckt vorher noch den Text, der in den Klammern steht |

### Beispiel
```python
lieblingsfarbe = input("Was ist deine Lieblingsfarbe?")
print("Deine Lieblingsfarbe ist " + lieblingsfarbe)
```
### Ausabe
```shell
> "Was ist deine Lieblingsfarbe?" lila
> Deine Lieblingsfarbe ist lila
```


# Datentypen

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| str() - String | Text | ```my_string = "Hallo"``` |
| int() - Integer | ganzzahlige Zahl | ```my_int = 3``` |

### Bespiel
```python
my_string = "Hallo"
my_int = 3
print(my_string + "Welt!") 
print(my_int + 2) 
```
### Ausgabe
```shell
> Hallo Welt
# Achtung das ist gleichzeitig eine Rechenoperation 3(my_int)+2=5
> 5
```

# Rechnen

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| + | addition | a + b |

### Beispiel
```python
var1 = 4
var2 = 6
summe = var1 + var2
```

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| - | subtraktion | a - b | 

### Beispiel
```python
var1 = 4
var2 = 6
differenz = var1 - var2
```

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| random.randint(min, max) | zufällige Zahll (Integer Wert) | generiert eine Zufallszahl; <br> min ist das kleinste mögliche Ergebnis, max das größtmögliche |

### Beispiel
```python
import random

# Irgendeine zufällige Zahl zwischen 1 und 10
zahl = random.randint(1,10)
print(str(zahl))
```

### Ausgabe
```shell
> 5
```

# Bedingungen

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| if/else | Bedingung:falls/andernfalls | if bedingung:<br>   befehle<br>else:<br>   befehle |

### Beispiel
```python
var = 5
if var > 0:
  print("positive Zahl")
else:
  print("negative Zahl") 
```
### Ausgabe
```shell
positive Zahl
```

# Vergleichen

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| \> und  \< | größer als und kleiner als | a < b |

### Beispiel
```python
var1 = 1
var2 = 2

if var1 > var2:     
   print("die erste variable ist größer")
```

### Ausgabe
```shell
die erste variable ist größer
```

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| \>= und \<= | größer gleich und kleiner gleich | a \>= ba \<= b |

### Beispiel
```python
var1 = 1
var2 = 1
if var1 <= var2:
  print("Die erste Variable ist nicht größer als die zweite")
```
### Ausgabe
```shell
Die erste Variable ist nicht größer als die zweite
```

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| == | vergleich "ist gleich" | a == b <br> !! das ist keine zuweisung |

### Beispiel
```python
if var1 == var2:
  print("gleich groß")
```

# Schleifen

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| while | während/ solange | while bedingung:<br>&nbsp;&nbsp;&nbsp;&nbsp;befehle | 

### Beispiel
```python
ziel = 5
while ziel > 0:
  print(str(ziel))
  ziel = ziel - 1
```

### Ausgabe
```shell
> 54321
```

| Name | Auf Deutsch | Definition |
| --- | --- | --- |
| for | für (jedes in einer Liste)mit range(n) kann man einfach hochzählen | for i in Liste:<br>&nbsp;&nbsp;&nbsp;&nbsp;Befehle |

### Beispiel
```python
for i in range(5):
  print(i)
```

### Ausgabe
```shell
> 0, 1, 2, 3, 4
```

# Debugging Checklist

- Überprüfe nochmal deinen Code auf Einrückungsfehler. Stimmt da alles?
- Wo speicherst du Variablen? Wann rufst du sie wieder auf?
- Welchen Datentyp haben deine Variablen? Musst du den gegebenfalls nochmal verändern?
- Lasse dir an wichtigen Schritten in deinem Programm per print() die Variablenwerte ausgeben.
- Ergeben deine Bedingungen (bei if bedingung) Sinn?

**Du kannst immer um Hilfe bitten**
