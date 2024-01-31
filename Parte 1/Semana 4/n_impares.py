n = int(input("Digite um valor: "))

i = 1

while n != 0:
    if i % 2 != 0:
        n = n - 1
        print(i)
    i = i + 1