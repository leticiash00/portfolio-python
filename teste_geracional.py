# Código feito para o usuário descobrir a qual geração pertence. 

print('Descubra a qual geração você pertence!')

ano = int(input('Em qual ano você nasceu? '))


if ano <= 1945:
    print('Você é da geração dos Veteranos!')
elif ano <= 1964:
    print('Você é um Baby Boomer!')
elif ano <= 1980:
    print('Você faz parte da Geração X!')
elif ano <= 1996:
    print('Você é um Millenial!')
elif ano <= 2010:
    print('Você faz parte da Geração Z!')
elif ano <= 2025:
    print('Você faz parte da Geração Alfa!')
else:
    print('Resposta inválida!')




