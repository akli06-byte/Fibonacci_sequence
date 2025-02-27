n = int(input("Combien de termes de la suite de Fibonacci souhaitez-vous afficher? "))
fib = [0, 1]

while len(fib) < n:
    fib.append(fib[-1] + fib[-2])

print(fib[:n])