from classe.car import Car 
from classe.bateria import Bateria

# HERANÇA #
class CarEletric(Car):
    """Representa aspectos específicos de veículos elétricos."""

    def __init__(self,make,model,year):

        """Inicializa os atributos da classe-pai."""
        super().__init__(make,model,year) 
        
        self.bateria= Bateria()
      

      
    


