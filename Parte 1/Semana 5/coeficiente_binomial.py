def fatorial (x):
    fat = 1
    while (x > 1):
        fat = fat * x
        x = x - 1
    return fat

n = int(input("Digite o primeiro numero: "))
k = int(input("Digite o segundo numero: "))

if k > n:
    print("Operação inválida. Repita a operação!")
else:
    coef = fatorial (n) / (fatorial (k) * (fatorial (n-k) ))
    print("O coeficiente binomial de", n, "na classe", k, "é", coef)