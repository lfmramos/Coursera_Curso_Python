import bubblesort
import contatempos
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return bubblesort.Ordenador()
    
    @pytest.fixture
    def lista_quase_ordenada(self):
        c = contatempos.ContaTempos()
        return c.lista_quase_ordenada(100)
    
    @pytest.fixture
    def lista_aleatoria(self):
        c = contatempos.ContaTempos()
        return c.lista_aleatoria(100)
    
    def lista_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i + 1]:
                return False
        return True
    
    def testa_bubblesort_aleatoria(self, o, lista_aleatoria):
        o.bolha_curta(lista_aleatoria)
        assert self.lista_ordenada(lista_aleatoria)
    
    def testa_selecao_direta_aleatoria(self, o, lista_aleatoria):
        o.selecao_direta(lista_aleatoria)
        assert self.lista_ordenada(lista_aleatoria)
        
    def testa_bubblesort_quase_ordenada(self, o, lista_quase_ordenada):
        o.bolha_curta(lista_quase_ordenada)
        assert self.lista_ordenada(lista_quase_ordenada)
    
    def testa_selecao_direta_quase_ordenada(self, o, lista_quase_ordenada):
        o.bolha_curta(lista_quase_ordenada)
        assert self.lista_ordenada(lista_quase_ordenada)