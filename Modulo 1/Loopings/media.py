# Solicite ao usuário 4 notas.
# Calcule a média
# Informe se o aluno está aprovado (media>=7), recuperação (5media<7) ou reprovado.
# Apresente as notas que o aluno tirou, a media e o status de sua situação

# lista
# for
# condicional


notas = [] # criei uma lista vazia que irá armazenar as notas recebidas

for i in range (4): # faz a pergunta 4 vezes
    nota = float(input(f'Informe a nota da prova {i+1}: '))
    if nota > 0: # só aceita nota positivas
        notas.append(nota)  # notas.append(nota) adiciona um elemento no final da lista
    else: # se a nota for negativa apresenta o print
        print('Valor inválido.')
print (f'Suas notas são: {notas}') # linha opcional
media = sum(notas)/len(notas) # a função sun(notas) somas todas as notas da lista
# a função len(notas) informa o tamanho da lista notas


if media >=7: # se a media for maior que 7
    print(f'Suas notas foram {notas}, sua {media: .2f} e você está aprovado.')
elif 5 <= media < 7: # se a media for de 5 a 6.99
    print(f'Suas notas foram {notas}, sua {media: .2f} e você está em recuperação.')
else: # notas abaixo de 5, ou seja, de 4.99 para baixo
    print(f'Suas notas foram {notas}, sua {media: .2f} e você está reprovado.')
# {media: .2f} formata a média para o resultado ter apenas 2 casas decimais