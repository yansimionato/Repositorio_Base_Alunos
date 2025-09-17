# Crie um programa que leia o peso de 5 pessoas. No final, mostre qual
# foi o maior e o menor peso lido.

# Etapas para resolução:
# 1) crie uma lista vazia para receber os pesos
# 2) crie um for para receber os pesos das 5 pessoas
# 3) adicione os pesos recebidos a lista
# 4) utilize a função max() e min() ou ordene a lista e busque o primeiro
# e o último elemento
# 5) apresente os resultados

pesos = []

for i in range (5):
    peso = float(input('Informe o seu peso em KG: '))
    pesos.append(peso)
print(f'A lista dos pesos em KG: ')

# maior_peso = max(pesos)
# menor_peso = min(pesos)

pesos.sort()
menor = pesos[0]
maior = pesos [-1]
# print(f'O maior peso é {maior_peso} KG e o menor peso é {menor_peso} KG. ')

print(f'O maior peso é {maior} KG e o menor peso é {menor} KG. ')