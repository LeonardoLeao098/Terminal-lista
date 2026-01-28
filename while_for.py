numeros = []

def ler_opcao():
    while True:
        try:
            return int(input('Escolha uma opção: '))
        except: ValueError
        print('Digite apenas números!')

def ler_numero():
    while True:
        try:
            return int(input('Digite o número a ser adicionado: '))
        except: ValueError
        print('Digite apenas números!')

def adicionar():
    new = ler_numero()
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

    escolha = ler_opcao()

    if escolha == 1:
        adicionar()
    elif escolha == 2:
        listar()
    elif escolha == 0:
        encerrar()
        break
    else:
        print('Opção inválida!')
    

