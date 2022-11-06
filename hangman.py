from io import open
from random import randint
from zipfile import ZipFile

# Schalte den DEBUG mode ein
# Damit kannst du bedingte Ausgaben in den Quellcode einbinden
# welche nicht ausgeführt werden wenn DEBUG = False ist
DEBUG = False
# Definiere die Auszugebenden Hangmanzeichnung
# siehe print_hangman()
HANGMAN = [
    """
       +++++++++++++++++++++++++++
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +                         +
       +                         +
       +                         +
       +                         +
       +                         +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +                         +
       +                         +
       +                         +
       +         ||              +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +                         +
       +         ||              +
       +         ||              +
       +         ||              +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /            +
       +         ||/             +
       +         ||              +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/             +
       +         ||              +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/       O     +
       +         ||              +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/       O     +
       +         ||        |     +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/      \\O/    +
       +         ||        |     +
       +         ||              +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """,
    """
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/      \\O/    +
       +         ||        |     +
       +         ||       / \\    +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       + {}        +
       +++++++++++++++++++++++++++
       """
]


def print_hangman(level=1000, print_errors=True):
    """
    Gebe das Galgenmännchen für den angegebenen Level auf die Konsole aus.
    Wenn der Level größer ist als die Anzahl der Felder in der Liste (HANGMAN) dann wird automatisch
    das letzte, vollständige Galgenmännchen verwendet.

    :param level: Die Anzahl der Fehler für die das Galgenmännchen gezeichnet werden soll
    :param print_errors:  Gibt an ob die Anzahl der Fehler im Galgenmännchen mit ausgegeben werden soll
    """
    lvl = min(level, len(HANGMAN) - 1)
    error_txt = "              "
    if print_errors:
        lvl_txt = f"{lvl}"
        if lvl < 10:
            lvl_txt = f" {lvl}"
        error_txt = f" Fehler: {lvl_txt} / {len(HANGMAN) - 1}"
    # verwendet die Funktion str.format um den Fehlertext in die Ausgabe einzubetten
    print(HANGMAN[lvl].format(error_txt))


def intro():
    """
    Gib eine Willkommensmeldung für das Spiel auf der Konsole aus.
    """
    print("""

             Willkommen
    Lass uns Galgenmännchen spielen

       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/       O     +
       +         ||       /|\\    +
       +         ||       / \\    +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       +++++++++++++++++++++++++++

    Wir haben ein Wort für sie ausgesucht!
       """)


def print_loosing_screen():
    """
    Gib die Verlierermeldung auf die Konsole aus.
    """
    print("""
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /      |     +
       +         ||/       O     +
       +         ||       /|\\    +
       +         ||       / \\    +
       +         ||              +
       +       ******            +
       +      ********           +
       +                         +
       +       VERLOREN!!!       +
       +++++++++++++++++++++++++++
       """)


def print_winning_screen():
    """
    Gib die Gewinnermeldung auf die Konsole aus.
    """
    print("""
       +++++++++++++++++++++++++++
       +         __________      +
       +         || /            +
       +         ||/             +
       +         ||              +
       +         ||              +
       +         ||       \\0/    +
       +       ******      |     +
       +      ********    / \\    +
       +                         +
       +       GEWONNEN!!!       +
       +++++++++++++++++++++++++++
       """)


def print_word(word, guessed_letters):
    """
    Gib das gesuchte Wort auf der Konsole aus. Bereits erratene Buchstaben werden angezeigt.
    Nicht erratenen Buchstaben werden mit einem '_' angezeigt.

    :param guessed_letters: Liste der bereits erratenen Buchstaben
    :param word: Das gesuchte Wort

    .. codeblock:: python

        print_word(word="Hallo", guessed_letter=['L'])
        print_word(word="Hallo", guessed_letter=['H'.'L'])

    Ausgabe:
    > Word: __ll_
    > Word: H_ll_
    """
    # Benutze die Funktion sort() von Listen um die erratenen Buchstaben alphabetisch zu sortieren.
    #
    guessed_letters.sort()
    print(f"Bereits erratene Buchstaben: {str(guessed_letters)}")
    # die Print Funktion hat einen optionalen Parameter 'end' der Standarmäßig einen Zeilenumbruch beinhaltet '\n'
    # Um den Zeilenumbruch nicht auszugeben setzen wir end auf den Leerstring "".
    print("Word: ", end="")
    # Gehe über jeden Buchstaben in Wort
    for letter in word:
        # Schaue nach ob der Buchstabe bereits erraten wurde
        if letter.upper() in guessed_letters:
            # wenn ja zeige ihn an. Gib keinen Zeilenumbruch am Ende aus
            print(letter, end="")
        else:
            # andernfalls zeige '_' an. Gib keinen Zeilenumbruch am Ende aus
            print("_", end="")
    print("")

    # Spezielle DEBUG ausgabe die das gesuchte Wort auf der Konsole ausgibt
    if DEBUG:
        print(f"DEBUG: {word}")


def read_words(file, zip_file_entry="german.dic"):
    """
    List die zu erratenen Wörter aus der angegebenen Wörterbuchdatei aus
    und speichert sie in eine interne Wörterliste.
    Die Datei enthält ein Wort pro Zeile.
    Wenn die Datei eine "zip" datei ist dann versucht die Funkion den angebenen Eintrag "zip_file_entry" aus
    der Datei zu lesen.
    :param file: Die Wörterbuchdatei als utf-8 kodierte Datei mit der Endung '.dic'.
    :param zip_file_entry: Der Name des Wärterbuches in der Zipdatei. Wird ignoriert
                           wenn es sich nicht um eine Zip Datei handelt.
    :return: Liste mit den geladenen Wörtern.
    """
    if file.endswith("zip"):
        # wenn es sich um eine Zipdatei handelt benutze die ZipFile klasse um das Wörterbuch zu lesen
        with ZipFile(file=file, mode="r").open(name=zip_file_entry, mode="r") as f:
            return read_lines(file=f, decode=True)
    else:
        # es handelt sich um eine "utf-8" kodierte Wörterbuchdatei
        with open(file=file, mode="r", encoding="utf-8") as f:
            # 'with ... as name' ist ein spezielles Pythonkommando welches Sicherstellt,
            # daß die Datei am Ende des Blocks geschlossen wird, selbst wenn innerhalb
            # des Blocks ein Fehler passiert.
            return read_lines(file=f)


def read_lines(file, decode=True):
    """
    Liest die angegebene Datei zeilen weise aus und gibt eine Liste aller Zeilen zurück.
    :param file: Die Textdatei welche gelesen wird
    :param decode: Gibt an ob es sich um einen Byte kodierte Datei handelt.
                   In diesem Fall handelt es sich um b-Strings welche erst dekodiert werden müssen.
    :return: Liste von Strings mit allen eingelesenen Zeilen.
    """
    result = []
    for line in file.readlines():
        if decode:
            _line = line.decode().strip()
        else:
            _line = line.strip()
        result.append(_line.upper())
    return result


def init_words(read_dicitonary=False):
    """
    Initialisert das interen Wörterbuch. Das Wörterbuch besteht aus einer Liste von Wörtern.
    Diese können entweder aus einer Datei ausgelesen werden oder es wird eine vorgegebene Liste erstellt.
    :param read_dicitonary: Sollen die Wörter aus der Datei "german.zip" ausgelesen werden.
    :return: Gibt die Liste der Wörter zurück
    """
    if read_dicitonary:
        return read_words(file="german.zip", zip_file_entry="german.dic")
    else:
        return [
            "Affe", "Kobold", "Terrarium", "Hallo Welt", "Programmierer",
            "Spieler", "Python", "Computer", "Hackerschool", "Schulkind",
            "Challenge"
        ]


def choose_word(words):
    """
    Wähle zufällig ein Wort aus dem Wörterbuch.
    :param words: Das Wörterbuch für die gesuchten Wörter
    :return: Das gewählte Wort
    """
    return words[randint(0, len(words) - 1)]


def guess_word(mistakes, word, guessed_letters):
    """
    Fragt nach einer Lösung für das Wort und gibt die Anzahl der Fehler zurück. Wird das Wort falsch geraten wird die
    Fehleranzahl hochgezählt.
    :param mistakes: Anzahl der Fehler
    :param word: Das gesuchte Wort
    :param guessed_letters: Liste mit den bereits erratenen Buchstaben
    :return: Die aktuelle Anzahl von Fehlern.
    """
    answer = input("Möchtest du das Wort erraten? (Tippe Ja):")
    if answer.upper() == "JA":
        entered_word = input("Wie lautet das Wort? ")
        # Wadle das eingebene Wort in Großbuchstaben und Vergleiche es mit dem gesuchten Wort in Großbuchstaben.
        if entered_word.upper() == word.upper():
            # Die Wörter sind gleich also fügen wir alle Buchstaben in die Liste der erratenen Buchstaben ein
            # damit die Siegbedingung erfüllt ist.
            for letter in entered_word:
                guessed_letters.append(letter.upper())
            return mistakes
        else:
            # Das Wort war falsch also erhöhen wir die Fehlerzahl um 1 und geben das Galgenmännchen aus.
            print("Schade! Du hast das Wort nicht erraten!")
            print_hangman(level=mistakes + 1)
            return mistakes + 1
    return mistakes


def enter_letter():
    """
    Fragt nach einem Buchstaben. Die Funktion stellt sicher das ein Buchstabe eingegeben wurde und
    gibt diesen dann zurück.

    :return: der eingegebene Buchstabe
    """
    # Wiederhole die Eingabe so lange bis wir einen gültigen Buchstaben erhalten
    while True:
        guessed_letter = input("Welchen Buchstaben möchtest du auswählen? ")
        if len(guessed_letter) != 1:
            # Wir haben mehr als einen Buchstaben erhalten
            print(f"Du hast mehr als einen Buchstaben eingegeben ('{guessed_letter}')! Bitte versuche es noch einmal!")
        elif not guessed_letter.isalpha():
            # Es handelt sich nicht um einen Buchstaben
            print(f"Bitte gib einen Buchstaben ein!")
        else:
            # Wir haben einen Buchstaben erhalten also verlassen wir die Eingabeschleife
            break
    return guessed_letter


def guess_letter(mistakes, word, guessed_letters):
    """
    Frage nach dem zu erratenden Buchstaben und prüft dann ob der Buchstabe im gesuchten Wort vorkommt. Wenn nicht
    oder der Buchstabe wurde bereits geraten, erhöhe die Fehlerzahl um eins. Kommt der Buchstabe im gesuchten Wort vor,
    füge ihn in die Liste der erratenen Buchstaben ein und gib die Fehlerzahl unverändert zurück.

    :param mistakes: Anzahl der Fehler
    :param word: Das gesuchte Wort
    :param guessed_letters: Liste der bereits erratenen Buchstaben
    :return: Die neue Fehleranzahl
    """
    # erfrage einen Buchstaben
    guessed_letter = enter_letter()
    # stell sicher, daß der eingegebene Buchstabe in Großbuchstaben ist
    letter = guessed_letter.upper()
    if letter in guessed_letters:
        print(f"Den Buchstaben '{guessed_letter}' hast du bereits erraten!")
        return mistakes + 1
    elif letter in word.upper():
        # Füge den Buchstaben ans Ende der Liste der erratenen Buchstaben ein
        guessed_letters.append(letter)
        print(f"Super!!!! Der Buchstabe '{guessed_letter}' kommt im gesuchten Wort vor!")
        return mistakes
    else:
        # Füge den Buchstaben ans Ende der Liste der erratenen Buchstaben ein
        guessed_letters.append(letter)
        print(f"Schade! Der Buchstabe {guessed_letter} kommt nicht im gesuchten Wort vor!")
        return mistakes + 1


def game_lost(mistakes):
    """
    Prüfe, ob das Spiel verloren ist. Das Spiel gilt als verloren, wenn die Anzahl der Fehler größer ist als die
    Anzahl der zu zeichnenden Galgenmännchen.

    :param mistakes: Anzahl der gemachten Fehler
    :return: True wenn das Spiel verloren ist ansonsten False
    """
    return mistakes >= len(HANGMAN) - 1


def game_won(word, guessed_letters):
    """
    Prüfe, ob das Spiel gewonnen ist. Das Spiel gilt als gewonnen, wenn alle Buchstaben des gesuchten Wortes in der
    Liste der zu erratenden Buchstaben vorkommt.

    :param word:
    :param guessed_letters:
    :return:
    """
    # Gehe Buchstabe für Buchstabe durch das Wort und schaue nach ob der Buchstabe erraten wurde
    for letter in word:
        if letter.upper() in guessed_letters:
            # Solange der Buchstabe vorkommt machen wir weiter
            continue
        # der Buchstabe wurde noch nicht erraten
        return False
    # Alle Buchstaben wurden gefunden
    return True


def is_game_finished(guessed_letters, mistakes, word):
    """
    Überprüfe, ob das Spiel gewonnen oder verloren wurde und falls ja, gib eine entsprechende Meldung aus.
    :param guessed_letters: Liste der bereits erratenen Buchstaben
    :param mistakes: Anzahl der gemachten Fehler
    :param word: Das gesuchte Wort
    :return: True wenn das Spiel gewonnen oder verloren wurde ansonsten False
    """
    if game_won(word=word, guessed_letters=guessed_letters):
        print(f"Super du hast das Wort '{word}' erraten!")
        print_winning_screen()
        return True
    elif game_lost(mistakes=mistakes):
        print(f"Schade du hast verloren! Das gesuchte Wort ist '{word}'!")
        print_loosing_screen()
        return True
    else:
        return False


def replay():
    """
    Frage nach ob erneut gespielt werden soll.
    :return: True wenn erneut gespielt werden soll ansonsten False.
    """
    answer = input("Möchtest du erneut spielen? Dann schreibe jetzt 'Ja':")
    if answer.lower() == "ja":
        return True
    else:
        return False


def play():
    """
    Das Spiel. Zunächst initialisieren wir das Wörterbuch, dann suchen wir ein Wort aus und geben eine
    Willkommensmeldung aus. Anschliessend starten wir die Spielschleife:

        1. Frage nach einem Buchstaben
        2. Gib das Galgenmännchen aus
        3. Gib den aktuellen Zustand des gesuchten Wortes aus
        4. Frage nach ob der Benutzer das Wort erraten möchte
        5. Prüfe nach, ob das Spiel gewonnen oder verloren wurde und brich das Spiel ab

    Wenn das Spiel beendet wurde, gib die Abschiedsmeldung aus.
    """
    words = init_words(True)
    run_game = True
    while run_game:
        mistakes = 0
        guessed_letters = []
        word = choose_word(words=words)
        intro()
        print_word(word=word, guessed_letters=guessed_letters)

        while not is_game_finished(guessed_letters=guessed_letters, mistakes=mistakes, word=word):
            mistakes = guess_letter(mistakes=mistakes,
                                    word=word,
                                    guessed_letters=guessed_letters)
            print_hangman(level=mistakes)
            print_word(word=word, guessed_letters=guessed_letters)

            # only ask if we have not guessed all letters yet
            if not game_won(word=word, guessed_letters=guessed_letters):
                mistakes = guess_word(mistakes=mistakes,
                                      word=word,
                                      guessed_letters=guessed_letters)
        # do we want to run again ?
        run_game = replay()

    print("Danke das du mit mir Galgenmännchen gespielt hast!")
    print("Bis zum nächsten mal.")


# Starte das Programm, wenn es von der Kommandozeile aufgerufen wurde. In diesem Fall beinhaltet __name__ den Wert
# '__main__'. Für all anderen Fälle beinhaltet __name__ den Namen der Datei ohne '.py' (= Modulname in unserem Fall
# 'hangman')
if __name__ == '__main__':
    play()
