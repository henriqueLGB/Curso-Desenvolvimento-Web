class Bateria():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self,bateria = 70):
        """Iniciliza os atributos da bateria."""

        self.bateria = bateria

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""

        print("O carro possuí " + str(self.bateria) + "-KWh de bateria")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria"""

        if self.bateria == 70 :
            range = 240
        elif self.bateria == 85: 
            range = 270

        message = "  O carro pode andar aproximadamente " + str(range) 
        message += " milhas sem abastecer "
        print(message)        
