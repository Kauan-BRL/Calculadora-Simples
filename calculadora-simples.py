from sys import exit

def soma(a,b):
    return a+b

def subtração(a,b):
    return a-b

def multiplicação(a,b):
    return a*b

def divisão(a,b):
    return a/b

if __name__ == '__main__':
    while True:
        print('''
=======================================
        Calculadora Simples
=======================================

Selecione uma operação:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Sair
    ''')

        while True:
            opção = int(input('Opção:'))

            if opção in {1,2,3,4,5}:
                while True:
                    if opção == 5:
                        exit('\nObrigado por usar a calculadora! Até a próxima.')
                    
                    n1 =int(input('Digite o primeiro número:'))
                    n2 = int(input('Digite o segundo número:'))

                    if opção == 1:
                        print(soma(n1,n2),'\n')
                        break
                    elif opção == 2:
                        print(subtração(n1,n2),'\n')
                        break
                    elif opção == 3:
                        print(multiplicação(n1,n2),'\n')
                        break
                    elif opção == 4:
                        print(divisão(n1,n2),'\n')
                        break
                break
            else:
                print('Digite opções válidas\n')

        while True:
            prox = input('Deseja realizar outra operação? (s/n):')

            if prox == 's':
                break
            elif prox == 'n':
                exit('\nObrigado por usar a calculadora! Até a próxima.')
            else:
                print('\nDigite opções válidas')
