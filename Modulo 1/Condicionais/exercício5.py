# Crie um código python que peça o valor da conta. Se for maior R$100,00
# adicione uma gorjeta de 10% e exiba o total a pagar.
# Caso contrário, adicione uma gorjeta de 5%.

conta_inicial = float(input("Digite o valor da conta: "))
if conta_inicial >= 100:
    valor_final = conta_inicial +(conta_inicial*0.1)
    print(f'Obrigada por sua visita, sua conta R$ {valor_final}. ')
else:
    valor_final = conta_inicial + (conta_inicial*0.05)
    print(f'Obrigada por sua visita, sua conta R$ {valor_final}. ') 