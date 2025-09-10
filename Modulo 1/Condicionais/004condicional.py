# 1) Crie um código em python que peça um número ao usuário e exiba "Numero par" se ele for divisível por 2.

# Etapas para resolução:
# 1) solicitar um número ao usuário
# 2) verificar se o número é par ou impar
# 3) informar se o número é par o impar

numero =float(input("Digite um numero: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.  ")
else:
    print(f"O número {numero} é impar.  ") 