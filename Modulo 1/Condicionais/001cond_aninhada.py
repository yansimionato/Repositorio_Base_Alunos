# 1. Identificação de número positivo, negativo ou zero 
# Crie um código em Python que leia um número e informe se ele é
# positivo, negativo ou zero

# 1) Entrada de dados
num = int(input("Digite um número inteiro: "))
# 2) Condicional para verificar se o número é maior ou igual a zero
if num >= 0:
    # condicional para checar se o número é zero
    if num == 0:
        print("O número digitado é zero.") # informa que o número é zero
    else: # informa que o número é positivo
        print(f"O número {num} é positivo.")
       # se o if for falso, entra no else e , informa que o número é negativo
else:
   print(f"O número {num} é negativo.")