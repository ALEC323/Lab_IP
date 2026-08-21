numero= 10
hexadecimal = ""
if numero == 0:
    print(0)
while numero > 0:
    hexadecimal = str(numero % 16) + hexadecimal
    numero = numero // 16    
print(hexadecimal)  