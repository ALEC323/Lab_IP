numero,binario = 8, ""   # numero es igual a 8 y el binario a cadena vacia
if numero == 0: print(0)   # si el numero es igual al 0 este se imprime 0
while numero > 0: binario,numero = str(numero % 2) + binario, numero // 2   #mientras el numero es mayor a 0, el binario es igual al residuo de la division entre 2 mas el binario y el numero es igual a la division entera del numero entre 2
print(binario) #se imprime el resultado de binario