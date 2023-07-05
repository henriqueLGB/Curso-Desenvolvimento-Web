# LISTA #

cores = ['vermelho','verde','amarela','azul']
print(cores)

#ACESSANDO ELEMENTOS DE UMA LISTA #

print(cores[0])
print(cores[1])
print(cores[-1]) # RETORNA O ÚLTIMO ELEMENTO DA LISTA #

# USANDO VALORES INDIVIDUAIS DE UMA LISTA #

print("Minha cor favorita é " + cores[-1].title())

# MODIFICANDO O ELEMENTO DE UMA LISTA # 
cores[0] = "rosa"
print(cores)

#ACRESCENTANDO ELEMETOS NA LISTA

cores.append('preto') # ADICIONA NO FINAL DA LISTA UM VALOR #
print(cores)

cores.insert(0,'roxo') # ADICIONA UM VALOR EM UMA POSIÇÃO ESPECÍFICA
print(cores)

# REMOVENDO ELEMENTOS DE UMA LISTA #

del(cores[0]) # COM O DEL ELE ELIMINA O ELEMENTO PERMANENTEMENTE DA LISTA, NÃO PODENDO SER ACESSADO NOVAMENTE #
print(cores)

corExcluida = cores.pop() # COM O POP PODEMOS ELEMINAR O ÚLTIMO ELEMENTO DA LISTA E ARAMZENA-LO EM UMA VARIÁVEL #
print(corExcluida)

# REMOVENDO UM ITEM DE  ACORDO COM O VALOR #

corExcluida = 'amarela'  # VALOR A SER EXCLUÍDO #

cores.remove(corExcluida) # REMOVE ESSE VALOR DA LISTA #
print(cores) 
print("\n A cor " + corExcluida + " foi removida da lista")


# ORDENANDO A LISTA COM O SORT() #
nomes = ['Julia','Henrique','Ana','Jose']
nomes.sort()

print(nomes)

# ORDENANDO A LISTA NA ORDEM REVERSA COM O SORT() #
nomes.sort(reverse=True)
print(nomes)

# ORDENANDO A LISTA TEMPORARIAMENTE COM A FUNÇÃO SORTED(), MAS NÃO AFETA A ORDEM ORINAL DA LISTA #
print(sorted(nomes))

# EXIBINDO UMA LISTA EM ORDEM INVERSA #
nomes.reverse()
print(nomes)

# DESCOBRINDO O TAMANHO DE UMA LISTA COM O LEN() #
print(len(nomes))



