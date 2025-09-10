# Se a pessoa tiver um convite válido, exiba "Entrada permitida", caso contrário, "Entrada negada".
codigo_convite = "vip"
convite_valido = input("Digite o código do convite").strip().lower()
if convite_valido == codigo_convite :
  print("Entrada permitida")
else:
  print("Entrada negada")
