# Crie um código python que peça o valor da conta. Se for maior R$100,00
# adicione uma gorjeta de 10% e exiba o total a pagar.
# Caso contrário, adicione uma gorjeta de 5%.

# Etapas para resolução
# 1) solicitar o valor da conta para o usuário
# 2) se a conta for maior que 100 adicionar 10% de gorjeta e apresentar o total a pagar
# 3) se a conta for menor que 100 adicionar 5% de gorjeta e apresentar o total a pagar

conta_inicial = float(input("Digite o valor da conta: "))
if conta_inicial >= 100:
    valor_final = conta_inicial +(conta_inicial*0.1)
    print(f'Obrigada por sua visita, sua conta R$ {valor_final}. ')
else:
    valor_final = conta_inicial + (conta_inicial*0.05)
    print(f'Obrigada por sua visita, sua conta R$ {valor_final}. ') 
