import forca
import adivinhacao


def start():
    print('(1) Adivinhacao')
    print('(2) Forca')
    game = int(input('Selecione o Jogo:\n > '))

    if (game == 1):
        adivinhacao.play()
    if (game == 2):
        forca.play()
    else:
        print('Opção invalida!')


if (__name__ == '__main__'):
    start()
