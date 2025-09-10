# Uma empresa concederá um aumento de salário aos seus funcionários,
# variável de acordo com o cargo, conforme a tabela abaixo:
# Cargo | Aumento (%)
# Programador de Sistemas | 30
# Analista de Sistemas | 20
# Analista de Banco de Dados | 15
# Crie um programa que solicite ao usuário o salário e o cargo de um
# determinado funcionário. Na sequência, o programa deve calcular e imprimir o
# seu novo salário. Caso o cargo informado não esteja na tabela, o programa
# deve imprimir "Cargo inválido".

# 1) Entrada dos dados
print("Relação de Cargos")
print("Programador | Analista de Sistema | Analista de Dados")

cargo = input("Por favor, informe seu cargo: ").strip().lower()


if cargo == "programador":
    salario = float(input("Informe seu salário mensal R$: "))
    salario_novo = salario * 1.30
    print(f"O novo salário do Programador é R$ {salario_novo}" )
elif cargo == "analista de sistemas":
    salario = float(input("Informe seu salário mensal R$: "))
    salario_novo = salario * 1.20
    print(f"O novo salário do Analista de Sistemas é R$ {salario_novo}" )
elif cargo == "analista de dados":
    salario = float(input("Informe seu salário mensal R$: "))
    salario_novo = salario * 1.15
    print(f"O novo salário do Analista de Dados é R$  {salario_novo: .2f}" )
else:
    print("Cargo não encontrado.")



