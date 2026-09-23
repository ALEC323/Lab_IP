while True:
        edad = int(input("edad: "))

        if 0<= edad<=120 and type(edad) ==int:
            break

        print("La edad debe estar entre 0 y 120 años.")
    except ValueError:
        print("Debes ingresar un número entero.")
    print(f"edad recibida: {edad}")

