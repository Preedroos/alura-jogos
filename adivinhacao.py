import random


def play():
    print('***********************')
    print('===== ADIVINHACAO =====')
    print('***********************')

    random_number = random.randrange(1, 101)
    score = 1000

    chances = select_mode()

    for times in range(1, chances + 1):
        guess = int(input('Adivinhe o número:\n > '))

        while (guess < 1 or guess > 100):
            guess = int(input('Adivinhe o número:\n > '))

        print(f'[ Tentativa {times} de {chances} ]')
        if (guess == random_number):
            print('SHOW!')
            break
        elif (guess < random_number):
            print('Dica: o número sorteado é MAIOR')
            dif = abs(guess - random_number)
            score -= dif
        elif (guess > random_number):
            print('Dica: o número sorteado é MENOR')
            dif = abs(guess - random_number)
            score -= dif
        else:
            print('não')

    print(f'\nSua pontuação final: {score} pontos!')


def select_mode():
    mode = 0

    while (mode == 0):
        print('(1) Fácil | (2) Médio | (3) Difícil')
        mode = int(input('Selecione a dificuldade:\n > '))

    if (mode == 1):
        chances = 10
    elif (mode == 2):
        chances = 5
    elif (mode == 3):
        chances = 3
    else:
        chances = 0

    return chances


if (__name__ == '__main__'):
    play()
