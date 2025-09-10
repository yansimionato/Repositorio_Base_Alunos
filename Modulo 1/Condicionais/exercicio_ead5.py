# Uma empresa de vendas deseja automatizar o cálculo de bônus de seus vendedores. 
# Cada vendedor recebe um bônus de 10% sobre o valor total das vendas, desde que tenha:

# - Alcançado mais de R$ 10.000,00 em vendas no mês e
# - Trabalhado pelo menos 20 dias úteis no mês

# Se não atender a essas condições, o bônus será de apenas 3% das vendas.
# Seu objetivo é escrever um programa que:
# - Receba como entrada o nome do funcionário, o valor total das vendas do mês, e o número de dias úteis trabalhados.
# - Calcule o valor do bônus conforme as regras acima
# - Exiba uma mensagem com o nome do funcionário, o valor das vendas, os dias trabalhados, e o valor do bônus.

def calcular_bonus(nome, vendas, dias_trabalhados):
  # Definir as condições para o bônus de 10%
  meta_vendas = 10000.00
  meta_dias = 20
  bonus_alto = 0.10  # 10%
  bonus_baixo = 0.03  # 3%
  
  # Calcular o bônus com base nas condições
  if vendas > meta_vendas and dias_trabalhados >= meta_dias:
    valor_bonus = vendas * bonus_alto
  else:
    valor_bonus = vendas * bonus_baixo
  
  return nome, vendas, dias_trabalhados, valor_bonus

if __name__ == "__main__":
  # Recebe a entrada do usuário
  nome_vendedor = input("Digite o nome do funcionário: ")
  vendas_mensais = float(input("Digite o valor total das vendas no mês: "))
  dias_uteis_trabalhados = int(input("Digite o número de dias úteis trabalhados: "))
  
  # Chama a função para calcular o bônus
  nome, vendas, dias, bonus = calcular_bonus(nome_vendedor, vendas_mensais, dias_uteis_trabalhados)
  
  # Exibe os resultados
  print("\n--- Relatório de Bônus ---")
  print(f"Funcionário: {nome}")
  print(f"Vendas no mês: R$ {vendas:.2f}")
  print(f"Dias trabalhados: {dias}")
  print(f"Valor do bônus: R$ {bonus:.2f}")