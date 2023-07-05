# FATIANDO UMA LISTA #
jogadores = ['Charles','martina','michael','florence','eli']

print(jogadores[0:3]) # PEGA OS TRÊS PRIMEIROS JOGADORES #
print(jogadores[1:4]) # PEGA OS TRÊS PRIMEIROS JOGADORES COMEÇANDO PELO MARTINA #
print(jogadores[:4])  # PEGA DO ÍNICIO ATÉ O QUARTO JOGADOR #
print(jogadores[2:])  # PEGA DO MICHAEL ATÉ O FINAL DA VÁRIAVEL #
print(jogadores[-3:]) # PEGA OS TRÊS ÚLTIMOS JOGADORES #

# PERCORRENDO UMA FATIA COM UM LAÇO #
for jogador in jogadores[:3]:
    print(jogador)

# COPIANDO UMA LISTA #
minhasComidas = ['Pizza','falafel','carrot cake']
comidasAmigos = minhasComidas[:] # COPIA À LISTA TODA, COMO COLOQUEI : SEM NENHUM PARAMÉTRO ELE COPIA A LISTA TODA

minhasComidas.append("cannoli")
comidasAmigos.append("ice cream")

print("Minhas comidas:")
print(minhasComidas)

print("Comidas dos meus amigos:")
print(comidasAmigos)

# TUPLA -> DEVE POSSUIR VALORES QUE NÃO DEVERÃO SER ALTERADOS #
dimensoes = (200,100)
print(dimensoes[0])
print(dimensoes[1])

# PERCORRENDO A TUPLA COM UM LAÇO #
for dimensao in dimensoes:
    print(dimensao)

# SOBRESCREVENDO A TUPLA #
dimensoes = (400,100)
for dimensao in dimensoes:
    print(dimensao)



