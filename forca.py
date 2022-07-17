import random
from turtle import clear


def play():
    word = chooseWord(importFile())
    is_beheaded = False
    is_right = False
    attempts = 6
    right_attempts = set()
    wrong_attempts = set()

    print('\n=======:GALLOWS:=======')

    drawAttempts(attempts)

    while not is_beheaded and not is_right:
        print(f'::. Fails [{display(wrong_attempts)} ]')
        print(f'::. Remains {attempts} of 6 attempts')
        print(f'::. Secret Word: {display(hiddenWord(word, right_attempts))}')
        guess = input('\nTry to guess a letter\n > ').upper().strip()

        clearCMD()

        if guess in word:
            right_attempts.add(guess)
        elif guess not in wrong_attempts:
            print(f"# Your guess '{guess}' isn't into the secret word!")
            wrong_attempts.add(guess)
            attempts -= 1
        drawAttempts(attempts)

        is_beheaded = attempts == 0
        is_right = '_' not in hiddenWord(word, right_attempts)

    if is_right:
        win_finish(word, right_attempts)
    else:
        lost_finish()


def importFile():
    words = []
    file = open('words.txt', 'r')
    for line in file:
        words.append(line.strip().upper())
    return words


def chooseWord(words: list):
    return words[random.randrange(len(words))]


def hiddenWord(word: list, right_attempts: set):
    index = 0
    hidden_word = ['_' for letter in word]
    for letter in word:
        if letter in right_attempts:
            hidden_word[index] = letter
        index += 1
    return hidden_word


def drawAttempts(attempts: int):
    file = open('attempts.txt', 'r', encoding='utf-8')
    char = file.readlines()
    end = attempts * 4
    start = end - 4
    if attempts == 6:
        print(f'\n{display(char[start:end:])}')
    if attempts == 5:
        print(f'\n{display(char[start:end:])}')
    if attempts == 4:
        print(f'\n{display(char[start:end:])}')
    if attempts == 3:
        print(f'\n{display(char[start:end:])}')
    if attempts == 2:
        print(f'\n{display(char[start:end:])}')
    if attempts == 1:
        print(f'\n{display(char[start:end:])}')
    if attempts == 0:
        print(f'\n{display(char[start:end:])}')
    file.close()


def win_finish(word: str, right_attempts: set):
    clearCMD()
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print(
        f'\n::. No More Secret Word: {display(hiddenWord(word, right_attempts))}')
    print('\nYou\'ve won!  :3')


def lost_finish():
    clearCMD()
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('\nYou\'ve lost!  o.O')


def display(self):
    string = ''
    for item in self:
        string += f' {item}'
    return string


def clearCMD():
    print('\n' * 100)


if (__name__ == '__main__'):
    play()
