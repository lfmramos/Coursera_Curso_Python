def fatorial(n):
    if n < 1:                       # base da recursÃ£o
        return 1
    else:
        return n * fatorial(n - 1)  # chamada recursiva