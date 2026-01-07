# Calculadora simples

# Entradas do usuário:

while True:
    
    try:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
    except ValueError:
        print('Apenas números são aceitos!')
        continue
    
    operacao = input('Digite a operação desejada(multiplicar = *, dividir = /, somar = +, subtrair = -): ')

# Operações:

    if operacao == '*':
        resultado = a * b
        
    elif operacao == '/':
        if b == 0:
            print('Não é possível realizar a divisão de um número por zero!')
            continue
        resultado = a / b
            
    elif operacao == '+':
        resultado = a + b
        
    elif operacao == '-':
        resultado = a - b
        
    else:
        print('Operação inválida! Você deve escolher entre (*, /, + ou -).')
        continue
        
    print(f'O resultado de {a} {operacao} {b} = {resultado:.2f}')
    
    retorno = input('Deseja fazer outro cálculo? (s/n) ').strip().lower()
    
    if retorno == 's':
        continue
    elif retorno == 'n':
        print('Calculadora encerrada!')
        break
    else:
        print('Opção inválida!')
        print('Calculadora encerrada automaticamente.')
        break
