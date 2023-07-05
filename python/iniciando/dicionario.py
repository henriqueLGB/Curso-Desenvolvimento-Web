# DICIONÁRIO SIMPLES #
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# ACESSANDO VALORES EM UM DICIONÁRIO #
novo_ponto = alien_0['points']
print("Sua pontuação atual é :" + str(novo_ponto))

#ADICIONANDO NOVOS CHAVE-VALORES #
alien_0['x_posicao'] = 0
alien_0['y_posicao'] = 25

print(alien_0)

#COMEÇANDO COM UM DICIONÁRIO VAZIO #
alien_1 = {}
alien_1['color']  = 'green'
alien_1['points'] = 5

print(alien_1)

#MODIFICANDO VALORES EM UM DICIONÁRIO #
print("Posição x atual do alien: " + str(alien_0['x_posicao']))
alien_0['x_posicao'] = 5
print("Posição x nova do alien :" + str(alien_0['x_posicao']))

#REMOVENDO VALROES DE UM DICIONÁRIO #
print(alien_0)
del alien_0['points']
print(alien_0)

#UM DICIONÁRIO DE OBJETOS SEMELHANTES #
favorite_language  =    {
                            'jen' : 'python',
                            'sarah' : 'c',
                            'edward': 'ruby',
                            'phil'  : 'python',
                        }

print("A linguagem favorita de Sarah é :" + favorite_language['sarah'].title())

# PERCORRENDO UM DICIONÁRIO COM UM LAÇO  (TODOS OS VALORES) #
user_0 = {'username':'efemi','first' : 'enrico','last' : 'fermi'}

for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# MÉTODO KEYS()  TRABALHA COM TODOS OS VALORES DE UM DICIONÁRIO #

for name in favorite_language.keys():
    print(name.title())

# PERCORRENDO AS CHAVES EM ORDEM USANDO LAÇO UTILIZANDO #

pessoas =   {
                'Henrique':22,
                'Ana':32,
                'Ricardo':54,
                'Eduardo':44,
                'Sara': 22,
            }

for name in sorted(pessoas.keys()):
    print("\n" + name.title())

# VALUES() DEVOLVE UMA LISTA DE VALORES SEM AS CHAVES #
for language in favorite_language.values():
    print(language.title())

#SET() FAZ COM QUE NÃO TENHA REPETIÇÃO NO DICIONÁRIO #
for language in set(favorite_language.values()):
    print("\n" + language.title())



