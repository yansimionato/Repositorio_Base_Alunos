# Crie um código python que verifique se 
# o ano é bissexto ou não

ano =  int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é bissexto.")
    else:
        print(f'O ano {ano} não é bissexto.')
else:
    print(f"O ano {ano} não é bissexto.")