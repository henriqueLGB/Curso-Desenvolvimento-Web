# PASSANDO UMA LISTA PARA FUNÇÃO #
def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista"""
    for name in names:
        msg = "Hello , " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty','margot']

greet_users(usernames)

# MODIFICANDO UMA LISTA EM UMA FUNÇÃO #
def print_models(unprinted_designs,completed_models):
    """
        Simula a impressão de cada design, até que não haja mais nenhum.
        Transfere cada design para completed_models após a impressão.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #SIMULA A CRIAÇÃO DE UMA IMPRESSÃO 3D A PARTIR DO DESIGN
        print("Priting model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


# EVITANDO QUE UMA FUNÇÃO MODIFIQUE UMA FILA UTILIZE O [:]#

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models  = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models[:])



