# Jogo "Adivinhe o número!"

import random

numero_secreto = random.randint(1,100)
tentativas = 0 

while True:
    
    try:
        palpite = int(input('Adivinhe o número secreto (de 1 a 100): '))
        tentativas += 1
    except ValueError:
        print('Opção inválida, você perdeu uma tentativa desnecessariamente!  Escolha um número.')
        continue
    
    if palpite > 100 or palpite < 1:
        print('Opção inválida, você perdeu uma tentativa desnecessariamente! Escolha um número de 1 a 100.')
    elif palpite == numero_secreto:
        print(f'Você acertou em {tentativas} tentativa(s)! O número é {numero_secreto}.')
        break
    elif tentativas == 7:
        print(f'Você perdeu: atingiu o número máximo de 7 tentativas! O número secreto era {numero_secreto}.')
        break
    elif palpite > numero_secreto:
        print('Não! O número secreto é menor que seu palpite.')
    elif palpite < numero_secreto:
        print('Não! O número secreto é maior que seu palpite.')
    
