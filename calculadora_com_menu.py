#Função MENU


def menu():

  while True:
    print('\n| Calculadora - Menu Principal |\n')
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = input('\nDigite o número da operação que deseja realizar: \n')

    if opcao in ('0', '1', '2', '3', '4'):
      return opcao
    else:
      print('\nOpção inválida! Digite um número entre 0 e 4.\n')



#Função PEDIR NÚMERO

def numeros_usuario():

  while True:

    try:
      numero = float(input('\nDigite um número: \n'))
      return numero
    except ValueError:
      print('\nEntrada inválida!\n')


#Funções OPERAÇÃO


def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  return a / b


#Programa principal


while True:
  escolha = menu()

  if escolha == '0':
    print('\nEncerrando a calculadora.\n')
    break

  a = numeros_usuario()
  b = numeros_usuario()

  if escolha == '1':
    print(f'\nO resultado de {a} + {b} = {soma(a, b)}\n')
  elif escolha == '2':
    print(f'\nO resultado de {a} - {b} = {subtracao(a, b)}\n')
  elif escolha == '3':
    print(f'\nO resultado de {a} * {b} = {multiplicacao(a, b)}\n')
  elif escolha == '4':
    if b == 0:
        print('\nÉ impossível dividir um número por zero!\n')
    else:
        print(f'\nO resultado de {a} / {b} = {divisao(a, b)}\n')

  print('\nRetornando ao menu principal...\n')

