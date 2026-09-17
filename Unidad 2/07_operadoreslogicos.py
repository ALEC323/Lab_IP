edad=19
tiene_credencial= True
tiene_adeudado= False

es_mayor= edad>=18
docuemntos_validos= tiene_credencial
sin_adeudo= not tiene_adeudado

autorizado= es_mayor and docuemntos_validos and sin_adeudo
print(autorizado)





