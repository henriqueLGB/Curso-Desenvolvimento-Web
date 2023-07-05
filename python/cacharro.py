from classe.dog import * 

#INSTÂNCIANDO A CLASSE E PASSANDO PARAMÊTROS
my_dog = Dog('pitoco',7)

# ACESSANDO ATRÍBUTOS DA CLASSE #
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old")

# ACESSANDO MÉTODOS #
my_dog.sit()
my_dog.roll_over()

print("\n\n")

# CRIANDO OUTRA INSTÂNCIA #
your_dog = Dog('lucy',11)

# ACESSANDO ATRÍBUTOS DA CLASSE #
print("My dog's name is " + your_dog.name + ".")
print("My dog is " + str(your_dog.age) + " years old")

# ACESSANDO MÉTODOS #
your_dog.sit()
your_dog.roll_over()
