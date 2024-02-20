def merge_sort(lista):
    if len(lista) <= 1:         # base da recursao
        return lista
    
    meio = len(lista) // 2
    
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])
    
    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:       # base da recursao
        return lado_direito
    
    if not lado_direito:        # base da recursao
        return lado_esquerdo
    
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
    
    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])