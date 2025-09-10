# Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu
# estoque em promoção, de acordo com a tabela a seguir:
# Condição de Pagamento | Desconto (%)
# À vista | 15
# Cartão de débito| 10
# Cartão de crédito | 5

print('Tabela de Formas de Pagamento')
print(" 1 - à vista (em espécie)")
print(" 2 - cartão de débito")
print(" 3 - cartão de crédito (vencimento)")

valor_venda = float(input("Informe o valor total da venda R$: "))
forma_pagamento = input("Informe a forma de pagamento (1|2|3): ")

if forma_pagamento == "1":
    valor_final = valor_venda * 0.85
    print(f"Obrigada pela sua compra, você recebeu um desconto e o valor final é R$ {valor_final}.")
elif forma_pagamento == "2":
     valor_final = valor_venda * 0.90
     print(f"Obrigada pela sua compra, você recebeu um desconto e o valor final é R$ {valor_final}.")
elif forma_pagamento == "3":
    valor_final = valor_venda * 0.95
    print(f"Obrigada pela sua compra, você recebeu um desconto e o valor final é R$ {valor_final}.")
else:
    print("Digite uma opção de pagamento válida.")