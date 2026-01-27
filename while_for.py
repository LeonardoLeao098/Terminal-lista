numeros = []

def adicionar():
    new = int(input('Digite o número a ser adicionado: '))
    numeros.append(new)
    print('Número adicionado!')

def listar():
    if not numeros:
            print('A lista está vazia.')
    else:
        contador = 1
        for numero in numeros:
            print(f'{contador}) {numero}')
            contador += 1

def encerrar():
    print('Encerrando...')
     
while True:
    print('\n1 - Adicionar número')
    print('2 - Listar números')
    print('0 - Sair\n')

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        adicionar()
    elif escolha == 2:
        listar()
    elif escolha == 0:
        encerrar()
        break
    else:
        print('Opção inválida!')
    

