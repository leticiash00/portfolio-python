def busca_usuario(nome, usuarios): 
    for usuario in usuarios: 
        if usuario['nome'].lower() == nome.lower(): 
            return usuario 
    return None


def cadastra(usuarios, novo_usuario):
    usuarios.append(novo_usuario)


def cria_usuario(nome, email, idade):
    usuario = {'nome': nome, 'email': email, 'idade': idade}
    
    return usuario


def menu():
    while True:
        print('\nMenu de opções\n')
        print('1 - Buscar usuário')
        print('2 - Listar usuários')
        print('3 - Cadastrar usuário')
        print('4 - Sair')

        opcoes_validas = ('1', '2', '3', '4')

        opcao = input('\nEscolha um número: \n')

        if opcao in opcoes_validas:
            return opcao
        else: 
            print('\nOpção inválida, tente novamente!\n')



def coordena_fluxo():
    usuarios = []
    
    while True:
        opcao = menu()

        if opcao == '1':
            nome_buscado = input('\nDigite o nome do usuário desejado: \n')
            usuario = busca_usuario(nome_buscado, usuarios)

            if usuario:
                print(f'\n-Nome: ',usuario['nome'])
                print(f'-Email: ',usuario['email'])
                print(f'-Idade: ',usuario['idade'])
            else: 
                print('\nUsuário inexistente!\n')
        elif opcao == '2':
            if len(usuarios) != 0:
                for usuario in usuarios:
                    print('-', usuario['nome'])
            else: 
                print('\nNão existem usuários cadastrados!\n')
        elif opcao == '3':
            while True:
                nome_usuario = input('\nDigite o nome do usuário que deseja cadastrar: \n')
                email_usuario = input('\nDigite o email do usuário que deseja cadastrar: \n')
                
                try:
                    idade_usuario = int(input('\nDigite a idade do usuário que deseja cadastrar: \n'))
                    break
                except ValueError:
                    print('\nDigite um número, por favor.\n')


            if busca_usuario(nome_usuario, usuarios):
                print('\nNome já cadastrado!\n')
            else:
                cadastra(usuarios, cria_usuario(nome_usuario, email_usuario, idade_usuario))
                print('\nUsuário cadastrado com sucesso!\n')
        else:
            print('\nEncerrando o sistema.\n')
            break
     
                

coordena_fluxo()
