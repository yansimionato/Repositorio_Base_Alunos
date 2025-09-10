# 3. Classificação por idade
# Faça um programa que leia a idade de uma pessoa e classifique-a em:
# criança: menor que 12 anos
# adolescente: entre 12 e 17 anos
# adulto: maior ou igual a 18 anos
# Utilize a estrutura de condicional aninhada

idade = int(input("Digite a sua idade"))

if idade > 0:
    if idade >= 18:
         print(f" você {idade} anos é um adulto. ")
    elif 12 <= idade <=17:
        print(f"você é {idade} anos é um adolescente. ")
    else:
        print(f"você tem {idade} anos e é uma criança.")
else: 
    print("Idade não pode ser negativa, digite uma idade válida.")
