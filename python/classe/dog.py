# CRIANDO UMA CLASSE DOG #

class Dog():

    """Uma tentativa simples de moldar um cachorro"""

    # MÉTODO INIT #
    def __init__(self,name,age):

        """Inicializa os atributos name e age"""
        self.name = name
        self.age  = age

    def sit(self):

        """Simula um cachorro sentando em resposta a um comando"""
        print(self.name.title() + " is not setting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(self.name.title() + " rolled over !")

