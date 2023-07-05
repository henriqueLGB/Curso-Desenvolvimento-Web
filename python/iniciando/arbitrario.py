# PASSANDO UM NÚMERO ARBITRÁRIO DE ARGUMENTOS COM * #

def make_pizza(*toppings):
    """Exibe a lista de ingrediente pedidos"""
    print("\n Making a pizza with the following toppings: ")
    for topping in toppings:
        print(" " + topping)

make_pizza('Pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# MISTURANDO ARGUMENTOS POSICIONAIS E ARBITRÁRIOS #

def making_pizza(size,*toppings):
    """Apresenta a pizza que estamos prestes a preparar"""
    print("\n making  a  " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

making_pizza(16,'queijo','tomate','calabresa','presunto')   

# USANDO ARGUMENTOS NOMEADOS ARBITRÁRIOS #
def build_profile(first,last,**user_info):
    """Constrói um dicionário contendo tudo que sabermos sobre um usuário"""
    profile = {}

    profile['first_name'] = first
    profile['last_name']  = last

    for key,value in user_info.items():
        profile[key] = value 

    return profile

user_profile = build_profile(   
                                "Albert","einstein",
                                location='Princeton',
                                field='physics'
                            )

print(user_profile) 