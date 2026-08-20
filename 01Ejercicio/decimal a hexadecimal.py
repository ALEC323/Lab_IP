numero = 10
valor ="0123456789ABCDEF"
while numero > 0:
    print(valor[numero % 16])
    numero = numero // 16    
