n = int(input("Digite um valor: "))

fator = 2

primo = True

if (n == 2) or (n == 1):
    print('primo')
else:
    while n % fator !=0 and fator <= n/2:
        fator = fator + 1
    if n % fator == 0:
        primo =  False
if primo == False:
    print("nao primo")
else:
    print("primo")