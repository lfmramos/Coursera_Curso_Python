numero = int(input("Digite um valor: "))
unidade = 0  
digitoIgual = False
while numero != 0 and not digitoIgual:   # while a condição for verdadeira, executa o bloco de comandos
    unidade = numero % 10   # Retorna o último número da sequência
    numero = numero // 10   # Retorna a sequência sem o último número
    if (numero % 10) == unidade:
        digitoIgual = True
if digitoIgual:
    print("sim")
else:
    print("não")

# quando a condição se tornar falsa, o while para de executar e pula para o próximo comando