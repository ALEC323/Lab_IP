while True:
    nombre = input("Nombre: ").strip()
   nombre= ""
for letra in nombreInput:
    if letra.isalpha():
        nombre += letra
    elif nombre:
        nombreInput= nombreInput.append

    if nombre and nombre.replace(" ", "").isalpha():
        break
        
    print("Usa letras y no dejes el nombre vacío.")

nombre_normalizado = nombre.title()
print(f"Hola, {nombre_normalizado}")

