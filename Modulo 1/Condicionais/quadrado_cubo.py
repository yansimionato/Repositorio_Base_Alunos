# Construa um programa que receba um número inteiro positivo informado pelo
# usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se
# ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve imprimir
# o valor calculado.


numero = int(input("Digite um número inteiro positivo: "))
if numero > 0:
        if numero % 2 == 0:
          quadrado = numero ** 2
          print(f"O número {numero} é par. O quadrado é {quadrado}.")
        else:
          cubo = numero ** 3
          print(f"O número {numero} é ímpar. O cubo é {cubo}.")
else:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")


