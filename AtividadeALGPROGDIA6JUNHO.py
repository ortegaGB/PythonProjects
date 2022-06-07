#Esse código estuda a ocorrência de palíndromos dado um inteiro positivo

def main():
    n = list(input())
    num_digitos = len(n)
    reverso = []
    myString = "".join(n)
    n = int(myString)
    valor_inicial = n
    for i in range(num_digitos):
        inverso = n % 10
        reverso.append(inverso)
        n = n // 10
    strings = [str(integer) for integer in reverso]
    myString2 = "".join(strings)
    revertido = int(myString2)
    if valor_inicial == revertido:
        print("%i é um palíndromo." %valor_inicial)
    else:
        print("%i não é um palíndromo." %valor_inicial)
main()