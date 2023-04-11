adj_list = [[1, 3], [2], [0], [4], [3], []]
start_node = 0
def reachable(adj_list, start_node):
    visitado = set()
    pila = [start_node]
    while pila:
        nodo = pila.pop(0)
        if nodo not in visitado:
            visitado.add(nodo)
            pila.extend(adj_list[nodo])
    return visitado

print(reachable(adj_list, start_node))