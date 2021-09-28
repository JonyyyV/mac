def graph_has_a_path(graph, start, end):
    # TODO: 
    # Programar el codigo esta funcion
    # Puedes definir funciones auxiliares si lo estimas oportuno
    
    path = [False] * len(graph);                        # Primero creamos un array de las dimensiones del grafo inicializada a False
    last = [start]                                      # Guardamos el valor start como last
    path[start] = True                                  # Colocamos la posicion del last a True dentro del array
    while len(last) != 0:                               # Utilizamos este bucle para recorrer todos los nodos hasta el start que hemos marcado como last
        for i in range(len(graph)):                     # Recorremos el grafo
            if(graph[last[0]][i] and path[i] == False): # En caso de que una posicion vecina al nodo este en False
                path[i] = True                          # la ponemos como True
                last.append(i)                          # y la anadimos a la lista de caminos escogidos
        last.remove(last[0])                            # Al salir del bucle de recorrer el grafo, eliminamos la primera posicion del last
        if(path[end]):                                  # En caso de que el valor end en nuestro grafo este a True
            return True                                 # devolvemos este resultado
    return False                                        # Solamente llegaremos a este caso si no hemos encontrado ningun camino, por lo que devolveremos False
         
def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 0, 1],
          [0, 1, 0, 0, 1],
          [0, 0, 1, 1, 0]]
    
    assert graph_has_a_path(g1, 0, 4)
    
    
    g2 = [[0, 1, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 1, 0]]
    
    assert graph_has_a_path(g2, 0, 1)
    assert not graph_has_a_path(g2, 0, 2)
    
    g3 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1],
          [0, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_a_path(g3, 1, 0)
    
    g4 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0]]
    
    assert graph_has_a_path(g4, 0, 5)
    
    g5 = [[0, 1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0]]
    
    assert graph_has_a_path(g5, 0, 5)

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
         
    assert  graph_has_a_path(g6, 0, 23)
                  

test()
