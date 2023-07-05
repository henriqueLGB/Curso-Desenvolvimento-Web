
message     = input("Digite seu nome: ")
idadeMinima = 22

try:

    idade = int(input("Digite sua idade: "))

except ValueError:

    print('Ocorreu um erro, por gentileza entrar em contato com Wilque')
    
else:   
    # idade = int(idade) #

    if (idade >= idadeMinima):
        print(message + ', Você pode votar')
    else:
        print(message + ', Você não pode votar')

finally:
    print('Teste finally')

# PÁGINA 168 #


