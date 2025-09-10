# Suponha que o professor Fábio possui 2 logins na rede acadêmica da
# instituição. Construa um programa que valide o acesso do professor à rede.
# Caso o par usuário/senha informado esteja correto, o programa deve imprimir a
# mensagem "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".

# Dados de login corretos
login_correto_1 = "fabio_ds"
senha_correta_1 = "fabiods123"

login_correto_2 = "fabio_web"
senha_correta_2 = "fabioweb321"

# Solicita o login e a senha ao usuário
login_digitado = input("Digite seu login: ")
senha_digitada = input("Digite sua senha: ")

# Verifica se o par de usuário/senha corresponde a um dos logins corretos
if (login_digitado == login_correto_1 and senha_digitada == senha_correta_1) or \
   (login_digitado == login_correto_2 and senha_digitada == senha_correta_2):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem.") 