# SEM PASSAGEM DE PARAMÉTROS #
from abc import abstractclassmethod


def greet_user():
    """"Exibe uma saudação simples"""  #Docstring#
    print("Hello")

greet_user()

# COM PASSGEM DE PARAMÉTRO #
def greet_user(username):
    """"Exibe uma saudação simples"""
    print("hello, " + str(username))

greet_user("Henrique")

# ARGUMENTOS POSICIONAIS #
def describe_pet(animal_type,pet_name):
    """Exibe informações sobre um animal"""
    print("\n I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')

#ARGUMENTOS NOMEADOS # 
def describe_pet(animal_type,pet_name):
    """Exibe informações sobre um animal"""
    print("\n I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry',animal_type='hamster') # DEFININDO O ARGUMENTAÇÃO #

#VALORES DEFAULT #
def describe_pet(pet_name,animal_type = 'dog'):
    """Exibe informações sobre um animal"""
    print("\n I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry')

#CHAMADAS DE FUNÇÃO EQUIVALENTES
def describe_pet(pet_name,animal_type = 'dog'):
    """Exibe informações sobre um animal"""
    print("\n I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry')

# DEVOLVENDO UM VALOR SIMPLES #
def get_formatted_user(first_name,last_name):
    """Devolve um nome completo formatado de modo elegante"""
    full_name = first_name + " " + last_name
    return full_name.title()

musico = get_formatted_user('jimi','hendrix')

print(musico)

# DEIXANDO UM ARGUMENTO OPCIONAL #
def get_formatted_name(first_name,last_name,middle_name = ''):
    """Devolve um nome completo formatado de modo elegante"""

    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:    
        full_name = first_name + " "  + last_name
    
    return full_name.title()

musico = get_formatted_name("john","lee")

print(musico)

# DEVOLVENDO UM DICIONÁRIO # 
def build_person(first_name,last_name,age = ''):
    """Devolve um diconário com informações sobre um pessoa"""

    person = {'first': first_name,'last':last_name}

    if age:
        person['age'] = age

    return person

musico = build_person('jimi','hendrix',27)

print(musico)

# USANDO UMA FUNÇÃO COM WHILE #
def get_formatted_name(first_name,last_name):
    """Devolve um nome completo formatado de modo elegante"""
    full_name = first_name + ' ' + last_name 
    return full_name.title()



while True:
    print("\nPlease tell your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name : ") 
    if f_name == 'q' : break

    l_name = input("Last name  : " )
    if l_name == 'q' : break

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + ' !')

