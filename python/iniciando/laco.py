# LAÇO FOR #
magicos = ['Alice','Jorge','Ana','Caio']

for teste in magicos :
    print("Tenha um bom show, " + teste)

print("Obrigado pelo Show Mágicos \n")

# FUNÇÃO RANGE #

for valor in range(1,6):
    print(valor)

#USANDO O RANGE PARA CRIAR LISTA NÚMERICA
listaNumerica = list(range(2,11,2))
print(listaNumerica)

# ESTATÍSTICA SIMPLES COM UMA LISTA DE NÚMEROS #
digitos = [1,2,3,4,5,6,7,8,9,0]

minimo = min(digitos)
maximo = max(digitos)
soma   = sum(digitos)

print(minimo)
print(maximo)
print(soma)

# LIST COMPREHESIONS #
quadrado = [value**2 for value in range(1,11)]
print(quadrado)
