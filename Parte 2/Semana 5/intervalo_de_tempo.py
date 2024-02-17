import time

# antes = time.time()
# algoritmo_a_ser_cronometrado()
# depois = time.time()
# print("A execução do algoritmo demorou ", depois - antes, "segundos")

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000) # Gera inteiros aleatórios entre 0 e 999
        return lista