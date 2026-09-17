total=float(input("total de la cuenta: "))
numero_de_personas =int(input ("número de personas: ")) 
propina=float(input("porcentaje de propina: "))

total_de_cuenta=(total+total*propina/100)
print(f"total con propina: {total_de_cuenta:.2f}")
total_por_persona=(total+total*propina/100)/numero_de_personas
print(f"total por persona: {total_por_persona:.2f}") 