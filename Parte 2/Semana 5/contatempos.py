import bubblesort
import random
import time

# antes = time.time()
# algoritmo_a_ser_cronometrado()
# depois = time.time()
# print("A execução do algoritmo demorou ", depois - antes, "segundos")

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)] # cria uma lista ordenada
        lista[n//10] = -500 # insere um valor fora de ordem na posição n//10
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
                
        o = bubblesort.Ordenador()
        
        print("Comparando com listas aleatórias")
        # antes = time.time()
        # o.bolha(lista1)
        # depois = time.time()
        # print("O algoritmo da bolha demorou ", depois - antes, "segundos.")
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("O algoritmo da bolha curta demorou ", depois - antes, "segundos.")
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("O algoritmo da seleção direta demorou ", depois - antes, "segundos.")
        
        print("\nComparando com listas quase ordenadas")
        
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        
        # antes = time.time()
        # o.bolha(lista1)
        # depois = time.time()
        # print("O algoritmo da bolha demorou ", depois - antes, "segundos.")
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("O algoritmo da bolha curta demorou ", depois - antes, "segundos.")
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("O algoritmo da seleção direta demorou ", depois - antes, "segundos.")