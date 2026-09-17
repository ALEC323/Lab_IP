edad=5
tiene_credencial= True
tiene_adeudado= False

if edad>=18:
    es_mayor= True
else:
    es_mayor= False
docuemntos_validos= tiene_credencial
sin_adeudo= not tiene_adeudado      

if es_mayor and docuemntos_validos and sin_adeudo:
    autorizado= True
else:
    autorizado= False
print(autorizado)