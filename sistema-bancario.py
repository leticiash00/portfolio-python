# Código construído para um sistema bancário simples, de apenas um usuário.  

menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opçao = input(menu)
    if opçao == '1':
        valor = float(input('Digite o valor desejado para o depósito: '))
        if valor > 0: 
            saldo += valor
            extrato += f'Depósito de R$ {valor: .2f}\n'
        else:
            print('Valor inválido!')
    elif opçao == '2':
        saque = float(input('Digite o valor do saque: '))
        if numero_saques == 3:
            print('Você excedeu o limite de saques!')                    
        elif saque <= saldo and saque < 500 and saque > 0:
            saldo -=saque
            extrato += f'Saque de R$ {saque: .2f}\n'
            numero_saques += 1
        elif saque > saldo:
            print('Você não possui saldo o suficiente!')
        elif saque > 500:
            print('O valor limite para saques é de R$500!')
        else:
            print('Valor inválido!')
    elif opçao == '3':
        print("\n--------------- EXTRATO ----------------")
        print("Nenhuma movimentação registrada" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------------------------")
    elif opçao == '0':
        break
    else:
        print('Opção inválida! ')


