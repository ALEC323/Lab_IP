numero,octal = 8, ""   # numero es igual a 8 y el octal a cadena vacia
if numero == 0: print(0)   # si el numero es igual al 0 este se imprime 0
while numero > 0: octal,numero = str(numero % 8) + octal, numero // 8   #mientras el numero es mayor a 0, el octal es igual al residuo de la division entre 8 mas el octal y el numero es igual a la division entera del numero entre 8
print(octal) #se imprime el resultado de octal