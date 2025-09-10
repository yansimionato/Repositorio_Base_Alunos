# copy()
# Dada a lista original = [1, 2, 3, 4], use .copy() para criar uma nova lista
# chamada copia. Altere a copia (adicione o número 99) e mostre as duas listas
# para verificar que são independentes.

original = [1, 2, 3, 4]
print(f'Lista original: {original}')

copia = original.copy()
print(f'Lista Cópia:{copia}')

copia.append(99)
print(f'Lista Cópia após o append:{copia}')