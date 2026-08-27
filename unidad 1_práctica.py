N = int(input("Proporciona un número: "))

if N <= 1:
    print("No es primo")

else:
    i = 2

    while i < N:
        if N % i == 0:
            print("No es primo")
            break
        i += 1
    else:
        print("Es primo")