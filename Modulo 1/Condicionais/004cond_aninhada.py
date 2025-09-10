# Tipo de triângulo
# Crie um programa que receba três lados de um triângulo
# verifique se os lados realmente pode formar um triângulo
# e determine os triângulos em:
# Equilatero (todos os lados são iguais)
# Isósceles (dois lados iguais)
# Escalenos (todos os lados diferentes)

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b "))
c = int(input("Digite o valor do lado c: "))

# Verificar se os lados formam um triângulo:
if a + b > c and a + c > b and b + c > a: # condição para formação do triângulo
    if a == b:
        if b == c:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Equilátero")
        else:
            print(f"Os lados do triângulo são {a}, {b} e {c}:Triângulo Isósceles.")
    else: # não é possível formar um triângulo
        if b == c or a == c:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo isósceles.")
        else:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Escaleno.") 
else:
    print("Os lados não foram um triângulo válido.")
    

