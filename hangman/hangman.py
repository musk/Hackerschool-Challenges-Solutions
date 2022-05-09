from io import open
from random import randint
from zipfile import ZipFile

DEBUG = False
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
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
       + {}          +
       +++++++++++++++++++++++++++
       """
]


def print_hangman(level=1000, print_errors=True):
    lvl = min(level, len(HANGMAN) - 1)
    error_txt = "              "
    if print_errors:
        error_txt = f" Fehler: {lvl} / {len(HANGMAN) - 1}"
    print(HANGMAN[lvl].format(error_txt))


def intro():
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


def print_word(solution, words, guessed_letters):
    if solution >= 0:
        guessed_letters.sort()
        print(f"Bereits erratene Buchstaben: {str(guessed_letters)}")
        print("Word: ", end="")
        solution_ = words[solution]
        for letter in solution_:
            if letter.upper() in guessed_letters:
                print(letter, end="")
            else:
                print("_", end="")
        print("")

        if DEBUG:
            print(f"DEBUG: {solution_}")
    else:
        raise ValueError("Game was not initilaized!")


def read_words(file):
    if file.endswith("zip"):
        with ZipFile(file=file, mode="r").open(name="german.dic",
                                               mode="r") as f:
            return read_lines(file=f, decode=True)
    else:
        with open(file=file, mode="r", encoding="utf-8") as f:
            return read_lines(file=f)


def read_lines(file, decode=True):
    result = []
    for line in file.readlines():
        if decode:
            _line = line.decode().strip()
        else:
            _line = line.strip()
        result.append(_line.upper())
    return result


def init_words(read_dicitonary=False):
    if read_dicitonary:
        return read_words("german.zip")
    else:
        return [
            "Affe", "Kobold", "Terrarium", "Hallo Welt", "Programmierer",
            "Spieler", "Python", "Computer", "Hackerschool", "Schulkind",
            "Challenge"
        ]


def init_game(words):
    guessed_letters = []
    hangman_lvl = 0
    solved = False
    solution = randint(0, len(words) - 1)
    return solution, hangman_lvl, solved, guessed_letters


def guess_word(level, words, solution, guessed_letters):
    word = input("Wie lautet das Wort? ")
    if word.upper() == words[solution].upper():
        for l in word:
            guessed_letters.append(l.upper())
        return level
    else:
        print("Schade! Du hast das Wort nicht erraten!")
        print_hangman(level=level + 1)
        return level + 1


def enter_letter():
    while True:
        guessed_letter = input("Welchen Buchstaben möchtest du auswählen? ")
        if len(guessed_letter) != 1:
            print(
                f"Du hast mehr als einen Buchstaben eingegeben ('{guessed_letter}')! Bitte versuche es noch einmal!"
            )
        elif not guessed_letter.isalpha():
            print(f"Bitte gib einen Buchstaben ein!")
        else:
            break
    return guessed_letter


def guess_letter(level, words, solution, guessed_letters):
    guessed_letter = enter_letter()
    letter = guessed_letter.upper()
    if letter in guessed_letters:
        print(f"Den Buchstaben '{guessed_letter}' hast du bereits erraten!")
        return level + 1
    elif letter in words[solution].upper():
        guessed_letters.append(letter)
        print(
            f"Super!!!! Der Buchstabe '{guessed_letter}' kommt im gesuchten Wort vor!"
        )
        return level
    else:
        guessed_letters.append(letter)
        print(
            f"Schade! Der Buchstabe {guessed_letter} kommt nicht im gesuchten Wort vor!"
        )
        return level + 1


def game_lost(errors):
    return errors >= len(HANGMAN) - 1


def game_won(words, solution, guessed_letters):
    for letter in words[solution]:
        if letter.upper() in guessed_letters:
            continue
        return False
    return True


def is_game_finished(guessed_letters, hangman_lvl, solution, words):
    if game_lost(errors=hangman_lvl):
        print(f"Schade du hast verloren! Das gesuchte Wort ist '{words[solution]}'!")
        print_loosing_screen()
        return True
    elif game_won(words=words,
                  solution=solution,
                  guessed_letters=guessed_letters):
        print(f"Super du hast das Wort '{words[solution]}' erraten!")
        print_winning_screen()
        return True
    else:
        return False


def replay():
    answer = input("Möchtest du erneut spielen? Dann schreibe jetzt 'Ja':")
    if answer.lower() == "ja":
        return True
    else:
        return False


def start():
    words = init_words(True)
    solution, hangman_lvl, solved, guessed_letters = init_game(words=words)
    intro()
    print_word(solution=solution, words=words, guessed_letters=guessed_letters)
    while not solved:
        hangman_lvl = guess_letter(level=hangman_lvl,
                                   words=words,
                                   solution=solution,
                                   guessed_letters=guessed_letters)
        print_hangman(level=hangman_lvl)
        print_word(solution=solution,
                   words=words,
                   guessed_letters=guessed_letters)

        answer = input("Möchtest du das Wort erraten? (Tippe Ja):")
        if answer.upper() == "JA":
            hangman_lvl = guess_word(level=hangman_lvl,
                                     words=words,
                                     solution=solution,
                                     guessed_letters=guessed_letters)

        if is_game_finished(guessed_letters=guessed_letters, hangman_lvl=hangman_lvl, solution=solution, words=words):
            if replay():
                solution, hangman_lvl, solved, guessed_letters = init_game(words=words)
                intro()
                print_word(solution=solution, words=words, guessed_letters=guessed_letters)
            else:
                break

    print("Danke das du mit mir Galgenmännchen gespielt hast!")
    print("Bis zum nächsten mal.")


if __name__ == '__main__':
    start()
