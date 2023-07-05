# CONTINUAÇÃO DO CAPITULO 6 #
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

# NESSA VARIÁVEL ARMAZENAREMOS AS LISTAS ACIMA #
aliens = [alien_0,alien_1,alien_2]

# PERCORRE O ARRAY #
for alien in aliens:
    print(alien)

#CRIANDO 30 ALIENS COM RANGE #
aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# MOSTRA OS 5 PRIMEIROS ALIENÍGENAS #
for alien in aliens[0:3]:
    print(alien)

# MOSTRA QUANTOS ALIENÍGENAS FORAM CRIADOS #
print('Total number of aliens: ' + str(len(aliens)))







