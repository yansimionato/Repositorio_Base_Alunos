# 2.Paridade e tamanho do número

# Crie um código que receba um número inteiro e informe:
# - se é par ou ímpar
# - e, ao mesmo tempo, se é maior que 10 ou menor ou igual a 10
# Utilize condicionais aninhadas para organizar as verificações

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0: # é par? se sim
    if numero > 10: # é maior que 10?
        print(f"O número {numero} é par e é maior que 10. ")
    elif numero == 10: # é igual a 10
        print(f"O número {numero} é par e igual a dez.")
    else: # é menor que dez
        print(f"o numero {numero} é par e menor que 10")
else: # não é par? se sim
    if numero >= 10:
         print(f"O número {numero} é impar e é maior que 10. ")
    else:
         print(f"O número {numero} é impar e é menor que 10. ")
   
