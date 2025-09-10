# Em sua programação semanal, uma rede de televisão apresenta os seguintes
# telejornais:
# - Bom Dia Nação, apresentado por Zé PINHEIRO e por Ana Carla ARAÚJO
# - Jornal Brasileiro, apresentado por Bill BONNER e CARLA VASCONCELOS
# Crie um programa no qual o usuário informe o sobrenome de um dos
# apresentadores. Se o sobrenome informado não estiver na lista acima, o
# programa deve mostrar a mensagem "Apresentador(a) desconhecido(a)". Em
# caso positivo, o programa deve mostrar o nome do telejornal apresentado pelo
# apresentador(a).

apresentadores = {
      "PINHEIRO": "Bom Dia Nação",
      "ARAÚJO": "Bom Dia Nação",
      "BONNER": "Jornal Brasileiro",
      "VASCONCELOS": "Jornal Brasileiro"
  }

sobrenome = input("Digite o sobrenome do(a) apresentador(a): ").upper()

if sobrenome in apresentadores:
    telejornal = apresentadores[sobrenome]
    print(f"O(a) apresentador(a) {sobrenome} apresenta o telejornal '{telejornal}'.")
else:
    print("Apresentador(a) desconhecido(a).")
