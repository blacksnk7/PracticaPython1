import random
num_aleatorio = random.randrange(100)
gane = False
print('Tenes 3 intentos para adivinar un numero entre 0 y 99')
intento = 0
while (intento < 5):
    num_ingresado = int(input('Ingresa tu numero '))
    if (num_ingresado == num_aleatorio):
        print('Ganaste! Y necesitaste {} intentos.'.format(intento))
        gane = True
    else:
        print('Numero equivocado. Segui intentando!')
        intento += 1
if not gane:
    print('\nPerdiste! \nEl numero buscado era: {}'.format(num_aleatorio))
        