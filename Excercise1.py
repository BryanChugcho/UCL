adj_mat = [[0, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0]]

def mat_to_list(matriz):
    n = len(matriz)
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                adj_list[i].append(j)
    return adj_list

adj_list = mat_to_list(adj_mat)
print(adj_list)


#'-----------------------------------------------------------------'

#def mat_to_list(matriz):
 #  3 lista = {}
 #   n = len(matriz)
  #  for i in range(n):
 #       lista[i] = []
 #       for j in range(n):
 #           if matriz[i][j] == 1:
  #              lista[i].append(j)
 #   return lista

#adj_mat = [[0, 1, 0, 1, 0, 0],
     #      [0, 0, 1, 0, 0, 0],
     #      [1, 0, 0, 0, 0, 0],
        #   [0, 0, 0, 0, 1, 0],
       #    [0, 0, 0, 1, 0, 0],
       #    [0, 0, 0, 0, 0, 0]]

#lista = mat_to_list((adj_mat))
#print(lista)