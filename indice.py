peso = float(input("peso: "))
estatura = float(input("estatura: "))
genero = input("hombre o mujer: ")
edad = int(input("Ingrese edad: "))

ForImc = peso / (estatura ** 2)

if genero == "mujer":
    if edad >= 19 and edad <= 24:
        if ForImc >= 18.9 and ForImc <= 25:
            print("Tu peso es optimo", ForImc)
        elif ForImc >= 25 and ForImc <= 29.6:
            print("Tienes obesidad", ForImc)

elif genero == "hombre":
    if edad >= 19 and edad <= 24:
        if ForImc >= 10.8 and ForImc <= 14.9:
            print("TTu peso es optimo", ForImc)
        elif ForImc >= 19.1 and ForImc <= 23.3:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 25 and edad <= 29:
        if ForImc > 18.9 and ForImc < 22:
            print("Tu peso es optimo", ForImc)
        elif ForImc >= 25.4 and ForImc <= 29.8:
            print("Tienes obesidad", ForImc)

elif genero == "hombre":
    if edad >= 25 and edad <= 29:
        if ForImc >= 12.8 and ForImc <= 16.5:
            print("Su peso es normal")
        elif ForImc >= 20.3 and ForImc <= 24.4:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 30 and edad <= 34:
        if ForImc >= 19.7 and ForImc <= 25.4:
            print("Su peso es normal")
        elif ForImc >= 26.4 and ForImc <= 30.5:
            print("Tienes obesidad", ForImc)
elif genero == "hombre":
    if edad >= 30 and edad <= 34:
        if ForImc >= 14.5 and ForImc <= 18:
            print("Su peso es optimo", ForImc)
        elif ForImc >= 21.5 and ForImc <= 25.2:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 35 and edad <= 39:
        if ForImc >= 21 and ForImc <= 24:
            print("Su peso es normal")
        elif ForImc >= 22.6 and ForImc <= 26.1:
            print("Tienes obesidad", ForImc)
elif genero == "hombre":
    if edad >= 35 and edad <= 39:
        if ForImc >= 16.1 and ForImc <= 19.4:
            print("Su peso es normal")
        elif ForImc >= 22.6 and ForImc <= 26.1:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 40 and edad <= 44:
        if ForImc >= 22.6 and ForImc <= 25.6:
            print("Su peso es normal")
        elif ForImc >= 29.3 and ForImc <= 32.8:
            print("Tienes obesidad", ForImc)
elif genero == "hombre":
    if edad >= 40 and edad <= 44:
        if ForImc >= 18.6 and ForImc <= 21.5:
            print("Su peso es normal")
        elif ForImc >= 24.5 and ForImc <= 27.6:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 45 and edad <= 49:
        if ForImc >= 24.3 and ForImc <= 27.3:
            print("Su peso es normal")
        elif ForImc >= 30.9 and ForImc <= 34.1:
            print("Tienes obesidad", ForImc)
elif genero == "hombre":
    if edad >= 45 and edad <= 49:
        if ForImc >= 18.6 and ForImc <= 24.5:
            print("Su peso es normal")
        elif ForImc >= 24.5 and ForImc <= 27.6:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 50 and edad <= 54:
        if ForImc >= 26.6 and ForImc <= 33.1:
            print("Su peso es normal")
        elif ForImc >= 32.8 and ForImc <= 37.5:
            print("Tienes obesidad", ForImc)
elif genero == "Hombre":
    if edad >= 50 and edad <= 54:
        if ForImc >= 19.8 and ForImc <= 26.2:
            print("Su peso es normal")
        elif ForImc >= 26.2 and ForImc <= 29.3:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 55 and edad <= 59:
        if ForImc >= 27.4 and ForImc <= 34:
            print("Su peso es normal")
        elif ForImc >= 35.1 and ForImc <= 37.3:
            print("Tienes obesidad", ForImc)
elif genero == "Hombre":
    if edad >= 55 and edad <= 59:
        if ForImc >= 20.2 and ForImc <= 26.2:
            print("Su peso es normal")
        elif ForImc >= 26.2 and ForImc <= 29.3:
            print("Tienes obesidad", ForImc)

if genero == "mujer":
    if edad >= 60:
        if ForImc >= 27.6 and ForImc <= 34.4:
            print("Su peso es normal")
        elif ForImc >= 34.5 and ForImc <= 38:
            print("Tienes obesidad", ForImc)
elif genero == "Hombre":
    if edad >= 60:
        if ForImc >= 20.3 and ForImc <= 26.7:
            print("Su peso es normal")
        elif ForImc >= 26.7 and ForImc <= 29.8:
            print("Tienes obesidad", ForImc)
