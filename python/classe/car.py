class Car:

    """Uma tentativa simples de representar um carro"""

    def __init__(self,make,model,year):
        """Inicializa os atributos que descrevem um carro"""
        self.make             =  make
        self.model            =  model
        self.year             =  year
        self.odometer_reading =  0

    def get_descriptive_name(self):
        """Devolve um nome descritivo,formatado de modo elegante"""
        long_name = str(self.odometer_reading) + ' ' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self,mileage):
        """Difine o valor de leitura do hodômetro com o valor espeficado"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("VocÊ deve digitar um valor maior que zero !")

    def increment_odomoter(self,miles):
        """Soma a quantidade especifica ao valor de leitura do hodômetro"""
        self.odometer_reading += miles


    