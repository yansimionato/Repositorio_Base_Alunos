# Se o valor da compra for maior que R$150,00, aplique um desconto de R$20,00. Caso contrário, não aplique desconto.

compra_inicial = float(input("Digite o valor da compra: "))
if compra_inicial >= 150:
    valor_final = compra_inicial - 20
    print(f'Obrigada por sua compra, valor R$ {valor_final}. ')
else:
    valor_final = compra_inicial 
    print(f'Obrigada por sua compra, valor R$ {valor_final}. ') 