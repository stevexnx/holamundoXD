intento = 0
while intento <= 3:
    print("determinar mayores")
    numero1 = input("escriba un numero: ")
    numero2 = input("escriba un numero mayor que el anterior: ")
    if numero1 >= numero2:
        print(numero2 +" no es mayor a " + numero1 )
    elif intento + 1:
        if numero1 < numero2:
            print(numero1 + " fue el menor y el mayor fue " + numero2 )
            print("programa terminado")     