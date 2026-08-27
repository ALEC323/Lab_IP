N = int(input("Proporciona un número: "))
if N <= 1:
    print("No es primo")
else:
    i = 2
    while i <= N:
        if N == 2:
            print("Es primo")
            break
        elif N % i == 0 and i != N:
            print("No es primo")
            break
        elif i == N and N % i == 0:
            print("Es primo")
            break
        i += 1