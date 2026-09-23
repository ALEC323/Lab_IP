while True:
    opcion = input("Elige A,B, o C:") 
    if opcion in ("A", "B", "C"):
        break

    print("Opción inválida, intenta de nuevo.")
print(f"Elegiste {opcion}.")