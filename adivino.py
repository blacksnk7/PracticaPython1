import random
num_aleatorio = random.randrange(101)
gane = False
print('Tenes 5 intentos para adivinar un numero entre 0 y 100')
intentos = 5
while (intentos > 0):
    num_ingresado = int(input('Ingresa tu numero '))
    if (num_ingresado == num_aleatorio):
        print('Ganaste! Y necesitaste {} intentos.'.format(intentos))
        gane = True
    else:
        intentos -= 1
        print('Numero equivocado. Te quedan {} intentos. Segui intentando!'.format(intentos))
if not gane:
    print('\nPerdiste! \nEl numero buscado era: {}'.format(num_aleatorio))
        