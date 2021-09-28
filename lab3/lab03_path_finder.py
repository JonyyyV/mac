def find_path(graph, start, end, path):
    # TODO
    # En este caso al ser un recursivo que recorre todas las posibilidades disponibles tenemos un algoritmo exponencial, el cual su peor orden seria de 2^n



    path.append(start)                              # Anadimos a la lista el nodo a analizar
    if start == end:                                # En caso de que el nodo en el que estamos sea el final, devolvemos el path que tengamos en ese momento
        return path                                 # de forma que comience el backtracking de la llamada
    else:                                           # Si no es el nodo final, tratamos el nodo
        for value in range (len(graph)):            # Recorremos la anchura del grafo
            if (graph[path[-1]][value] == 1):       # En caso de que nuestro nodo tenga conexion con algun otro, tratamos ese camino
             if value not in path:                  # En caso de que el nodo a tratar ya haya sidos seleccionado, no lo escogemos
                find_path(graph, value, end, path)  # Si ese nodo no ha sido tratado, se hace una llamada recursiva usando ese nodo como start.
                if (path[-1] == end):               # En caso de que el ultimo valor del path sea el destino final
                    return path                     # devolvemos el path
                else:                               # Si no lo es, eliminamos esa ultima posicion, ya que no nos sirve para nuestro camino
                    path.remove(path[-1])
        return []                                   # Este return solamente sera llegado en caso de que no exista ningun camino, devolviendolo vacio
            
    
def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 0, 1],
          [0, 1, 0, 0, 1],
          [0, 0, 1, 1, 0]]
    
    assert find_path(g1, 0, 4, []) in [[0, 2, 4], [0, 2, 1, 3, 4], [0, 1, 2, 4], [0, 1, 3, 4]]
    
    g2 = [[0, 1, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 1, 0]]
    
    assert find_path(g2, 0, 1, []) in [[0,1]]    
    assert find_path(g2, 0, 2, []) == []
    
    g3 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1],
          [0, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert find_path(g3, 1, 0, []) in [[1, 3, 2, 0], [1, 3, 5, 4, 2, 0]]
    
    g4 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0]]
    
    assert find_path(g4, 0, 5, []) in [[0, 2, 5]]

    g5 = [[0, 1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0]]
    
    assert find_path(g5, 0, 5, []) in [[0, 4, 5]]
    
def test2():
    
    g6 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
         
    print(find_path(g6, 0, 23, []))
         
test()
#test2()

