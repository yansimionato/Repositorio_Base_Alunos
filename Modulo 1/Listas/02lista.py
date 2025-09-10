# Dada a lista de números = [1, 2, 3], use .extend()
# para adicionar os elementos de outra
# lista mais_numeros = [4, 5, 6].
# Mostre o resultado.

# RESOLVIDO

numeros = [1, 2, 3]
print(numeros)
mais_numeros = [4, 5, 6] # nova variavel
# recebe uma lista
numeros.extend(mais_numeros) # extende a lista numeros
print(numeros)