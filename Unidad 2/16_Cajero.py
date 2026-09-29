def consultar_saldo():
    print("Saldo: $0.00")
def depositar():
     print("Deposito realizado")
def retirar():
    print("Retiro realizado")
def salir():
     print("Saliedo del cajero automatico...")

def mostrar_menu():
    print("Bienvenido al cajero automatico")
    print("1.Consular saldo")
    print("2.Depositar")
    print("3.Retirar")
    print("4.Salir")
    return input ("opcion").strip()

def main():
    while True:
         opcion= mostrar_menu()
         if opcion == "1":
          consultar_saldo()
         elif opcion== "2":
          depositar()
         elif opcion== "3":
          retirar()
         elif opcion=="4":
          salir()
         break
    else:
        print ("opcion invalida")

main()

  
