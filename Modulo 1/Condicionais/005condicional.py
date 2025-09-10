# Crie um ´código Python que verifique se a senha digitada pelo usuário for "1234", exiba "Acesso permitido"

# Etapas para resolução:
# criar um variavel e a atribuir a ela uma senha 
# através de imput solicitar a senha ao usuário
# através da condicional checar se a senha é igual a senha armazenada
# liberar ou não o acesso ao usuário

senha_usuario = "4567"
senha = input("Digite sua senha: ")
if senha_usuario == senha :
    print("acesso liberado")
else:
    print("acesso negado. tente novamente")
