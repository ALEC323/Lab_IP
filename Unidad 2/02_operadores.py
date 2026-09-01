operador = input("inserta un operador (+,-,*,/): ")
if operador == "+":
    O1 = input("ingresa un numero: ")
    O2 = input("ingresa otro numero: ")
    resultado =(O1) + operador + (O2)
    print(eval(resultado))