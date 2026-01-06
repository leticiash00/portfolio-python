import random

while True:
    jogar = input('Quer jogar o dado?(S/N): ')
    if jogar == 'S':
        print(f'Você jogou o dado! A face voltada para cima é de número {random.randint(1,6)}.')
    else:
        break
