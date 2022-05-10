from random import randint


def guess_my_number():
    """
    Startet das Spiel.
    """
    minimum = 1
    maximum = 100
    # Wähle eine zufällige Zahl zwischen minimum und maximum
    geheime_zahl = randint(minimum, maximum)
    versuche = 1
    e = ""

    print(
        f"Ich habe mir eine Zahl ausgedacht. Es ist eine Zahl zwischen {minimum} und {maximum}. Kannst du sie erraten?")

    # Starte die Spielschleife
    while True:
        eingabe_nutzer = input("Bitte gib eine Zahl ein: ")
        # überprüfe, ob es sich bei dem eingebenen Text um eine Zahl handelt mittels der Funktion str.isnumeric()
        if not eingabe_nutzer.isnumeric():
            # die Eingabe war keine Zahl springe zurück zum Anfang der Schleife
            print("Das ist keine Zahl!")
            continue

        if int(eingabe_nutzer) < geheime_zahl:
            print("Das ist leider falsch. Meine Zahl ist größer!")
        elif int(eingabe_nutzer) > geheime_zahl:
            print("Das ist leider falsch. Meine Zahl ist kleiner!")
        else:
            print(f"Das ist richtig! Du hast {versuche} Versuch{e} gebraucht")
            break

        print("Versuch es nochmal")
        versuche += 1
        e = "e"


# Starte das Programm, wenn es von der Kommandozeile aufgerufen wurde. In diesem Fall beinhaltet __name__ den Wert
# '__main__'. Für all anderen Fälle beinhaltet __name__ den Namen der Datei ohne '.py' (= Modulname in unserem Fall
# 'uebung3')
if __name__ == '__main__':
    guess_my_number()
