letra = 's'

while letra == 's': # o código será executado enquanto o usuário permanecer indicando que sim (s)
    n1 = float(input('Digite um número:'))
    n2 = float(input('Digite a porcentagem que deseja descobrir: '))

    porcentagem = (n1*n2)/100
    print(f'A porcentagem é igual a : {porcentagem}')
    letra = input("Deseja continuar? (s/n): ").lower()