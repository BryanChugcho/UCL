def mat_to_list(matriz):
    lista = {}
    n = len(matriz)
    for i in range(n):
        lista[i] = []
        for j in range(n):
            if matriz[i][j] == 1:
                lista[i].append(j)
    return lista

adj_mat = [[0, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0]]

adj_list = mat_to_list(adj_mat)

for i in range(len(adj_list)):
    print(f"Node {i} is connected with the nodes: {adj_list[i]}")