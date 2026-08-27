numero,hexadecimal= 10, ""
if numero == 0: print(0)
while numero > 0:
    numero = numero // 16    
    hexadecimal = str(numero % 16) + hexadecimal
    numero = numero // 16    
print(hexadecimal)  