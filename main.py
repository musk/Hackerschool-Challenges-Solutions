import sys

import hangman
import uebung3


def input_numeric(prompt, max_option):
    """
    Wartet auf die Eingabe einer Zahl.

    :param prompt: Text auf der Konsole für die Eingabe
    :return: Die eingebene Zahl.

    .. codeblock:: python

        zahl = input_numeric("Wie lautet deine Zahl? ")
        print(zahl)

    Ausgabe:
        > Wie lautet deine Zahl? a
        Bitte geben sie eine Zahl ein!
        > Wie lautet deine Zahl? 1
        1
    """
    while True:
        _in = input(prompt)
        # input gibt immer einen String zurück. Wir nutzen die Funktion str.isnumeric() um zu überprüfen, ob die
        # Eingaben eine Zahl ist.
        if _in.isnumeric():
            # wir haben eine Zahl also können wir sie mit int() in den Typen int (=Ganzzahl) umwandeln.
            ret = int(_in)
            if ret <= max_option:
                return ret
        print("Bitte geben sie eine gültige Zahl ein!")


def print_help():
    print(f"""
Dies sind Lösungsvorschläge für die Übungen und die erweiterten Challenges aus dem Hackerschoolkurs
"Spiele mit Python". Um den Quellcode einzusehen musst du in die entsprechende PYthondatei wechseln. Um das Spiel
zu spielen wähle das Spiel aus.

Drück die 'Enter'-Taste um fortzufahren
""")
    sys.stdin.read(1)


def main():
    """
    Unser Hauptprogramm.
    1. Gib das Menü aus
    2. Frage nach der Auswahl
    3. Führe die Auswahl aus.
    """

    # Unser Menü wird als eine Liste von Dict Objekten (Dictionray = HashMap oder assoziative Liste) definiert. Das
    # Dict besteht aus einer Liste von Schlüssel und Werte Paaren. Mit Hilfe des Schlüssels kann ich den
    # entsprechenden Wert aus dem Dict auslesen.
    #
    # Beispiel:
    # woerterbuch = { "a": "Der Buchstabe A", "b": "Der Buchstabe B" }
    # woerterbuch["a"] == "Der Buchstabe A
    # woerterbuch["b"] == "Der Buchstabe B
    games = [
        # Der Name des Menüeintrages
        {"name": "Galgenmännchen",
         # Der Code um das Programm zu starten (modul.funktion())
         "start": f"{hangman.__name__}.play()",
         # Die Datei, in welcher der Quellcode zu finden ist
         "file": "hangman.py"},
        {"name": "Rate Meine Nummer",
         "start": f"{uebung3.__name__}.guess_my_number()",
         "file": "uebung3.py"}
    ]

    while True:

        print("""
***************************************************************
*      Menü                                                   *
***************************************************************""")
        format_str = "*% 3s | %-25s  | %-26s*"
        # Iteriert der Reihe nach über die Einträge des Woerterbuchs. Die Funktion enumerate() gibt dabei immer den
        # aktuellen Schlüssel und den dazugehörigen Wert als Paar zurück.
        print(format_str % ("", "Name", "Python-Datei"))
        print("*  ---------------------------------------------------------  *")
        for idx, value in enumerate(games):
            # Füge den Schlüssel und den Namen des Spiels in den Menütext ein
            print(format_str % (idx, value["name"], value["file"]))
        print(format_str % (len(games), "Hilfe", ""))
        print(format_str % (len(games) + 1, "Exit", ""))

        print("""***************************************************************
""")
        # Frag nach dem Spiel
        idx = input_numeric("> ", len(games) + 1)
        if 0 <= idx < len(games):
            # Die Eingabe referenziert einen Eintrag in der Liste
            exec(games[idx]['start'])
        elif idx == len(games) + 1:
            # Exit
            break
        elif idx == len(games):
            print_help()


# Starte das Programm, wenn es von der Kommandozeile aufgerufen wurde. In diesem Fall beinhaltet __name__ den Wert
# '__main__'. Für all anderen Fälle beinhaltet __name__ den Namen der Datei ohne '.py' (= Modulname in unserem Fall
# 'main')
if __name__ == "__main__":
    main()
