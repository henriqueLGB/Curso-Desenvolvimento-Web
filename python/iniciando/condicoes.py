# CONDIÇÃO IF COM LAÇO #
carros = ['audi','bmw','subaru','toyota']

for carro in carros:

    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())

# VERIFICANDO UM VALOR EM UMA LISTA #
pizzaria = ['mushrooms','onions','pineapple']

print('mushrooms' in pizzaria)
print('apple'     in pizzaria)

# VERIFICANDO SE UM VALOR NÃO ESTÁ NA LISTA #
usuarios_banidos = ['Wilque','Lucas','Caio']

usuario = 'Henrique'

if usuario not in usuarios_banidos:
    print("Você pode digitar um comentário " + usuario.title())
else:
    print("Atenção, você está banido !")

# IF,ELIF E ELSE #
frutas = ['Maça','Banana','uva','Pera']

if 'abacaxi' in frutas:
    print("Abacaxi")
elif 'Banana' in frutas:
    print("Banana")
else:
    print("Erro")


# PÁGINA 130 #
