def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

def pertenceFibonacci(numero, sequencia):
    return numero in sequencia

numero = int(input("Digite um número: "))
sequencia_fibonacci = fibonacci(numero)

if pertenceFibonacci(numero, sequencia_fibonacci):
    print(f"O número {numero} pertence.")
else:
    print(f"O número {numero} não pertence.")