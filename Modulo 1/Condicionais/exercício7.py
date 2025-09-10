# Peça ao usuário para digitar "M" para manhã ou qualquer outra tecla para tarde. Se for "M", "Bom dia!", senão exiba "Boa tarde!".

# Pede ao usuário para digitar uma opção
turno = input("Digite 'M' para manhã ou qualquer outra tecla para tarde: ")

# Converte a entrada para maiúscula para evitar erros de digitação
turno = turno.upper()

# Verifica a opção do usuário
if turno == 'M':
    print("Bom dia!")
else:
    print("Boa tarde!")