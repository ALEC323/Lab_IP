numero = 10; hexadecimal = "0" if numero == 0 else ""; 
while numero > 0: 
    residuo = numero % 16; 
    hexadecimal = ("ABCDEF"[residuo - 10] if residuo >= 10 else str(residuo)) + hexadecimal; 
    numero //= 16
print(hexadecimal)

