from time import time

# vertex_cover_tree inicializa y llama al arbol de busqueda
def partial_validity_check(cover, graph):
    # TODO: Programa el codigo de la funcion
    for i in range(len(graph)):                                         # Recorremos con ambos for's la totalidad del grafo
          for j in range(len(graph)):
              if j!=i:                                                  # En las posiciones en las que i y j no sean iguales, ya que es el mismo nodo
                  if graph[i][j]==1 and cover[i]==0 and cover[j]==0:    # En caso de que esa posicion tenga un 1 y ambos cover's sean igual a 0
                      return False                                      # devolvemos False, por lo que dejamos de buscar
    return True    

def vertex_cover_tree(graph):
    n = len(graph)
    cover = [None]*n
    return recursive_vertex_cover(graph, cover)

def construir(cover, graph):                                             
    for i in range(len(cover)):                                         # Recorremos todas las posiciones del cover
        if cover[i] == None:                                            # En caso de que encontrar un nodo vacio
            for j in range(len(graph)):                                 # Recorremos todas las posiciones del grafo
                if j!=i and graph[i][j]==1 and cover[j]==0:             # y en caso de encontrar una posicion, que no sea el nodo mismo, que el valor del cover sea 0
                    cover[i]=1                                          # y que el valor del grafo este a 1, cambiamos el valor del cover
            if cover[i]==None:                                          # En caso de que tras tratarlo siga siendo None el nodo
                cover[i]=0                                              # cambiamos su valor a 0
                    
    return cover                                                        # Tras el tratado del cover, lo devolvemos

def recursive_vertex_cover(graph, cover):

    ############
    # TODO: Programa esta parte de la funcion
    #
    # Comprueba es posible construir un cover valido.
    # Si no es posible, devuelve [1]*len(cover).
    # En otro caso, encuentra dos nodos u y v conectados y que no estan en el cover.
    # Si no los hay, completa el cover decidiendo si los que faltan deben formar parte
    # del cover o no y una vez hecho esto, devuelve el cover completo.
    # En otro caso continua con u y v

    # Final de tu codigo
    # Lo siguiente abre las tres ramas del arbol de busqueda.
    # No modificar nada.
    ##############
    u, v = -101, -101                                                        # Comenzamos inicializando a un numero inalcanzable dos flag's
    if not partial_validity_check(cover, graph):                             # Llamamos a la funcion que comprueba si es posible la creacion del cover                                     
        return [1]*len(cover)                                                # En caso de que no sea posible, devolvemos lo exigido, [1]*len(cover)
    else:                                                                    # Si es posible
        for i in range(len(cover)):                                          # recorremos todo los nodos del grafo
            if cover[i] == None:                                             # En caso de que encontremos un nodo que se encuentra vacio
                for j in range(len(cover)):                                  # Recorremos toda la anchura de ese nodo
                    if i != j and cover[j] == None and graph[i][j] == 1:     # En una posicion que no sea el mismo nodo, si el nodo es vacio y el grafo es conexo
                        u = i                                                # Guardamos la posicion de anchura
                        v = j                                                # y la posicion de la altura
                        break                                                # y terminamos el bucle
                if u != -101:                                                # Si no encontramos una posicion valida
                    break                                                    # tambien salimos del bucle
        if u == -101:                                                        # En caso de que el cover pueda ser construido
            return construir(cover, graph)                                   # llamamos a la funcion que completa el cover


        copy_cover = list(cover)
        cover[u] = 1
        cover[v] = 0
        c10 = recursive_vertex_cover(graph, cover)
        cover = list(copy_cover)
        cover[u] = 0
        cover[v] = 1
        c01 = recursive_vertex_cover(graph, cover)
        cover = list(copy_cover)
        cover[u] = 1
        cover[v] = 1
        c11 = recursive_vertex_cover(graph, cover)
        if c10.count(1) <= min(c01.count(1), c11.count(1)):
            return c10
        elif c01.count(1) <= c11.count(1):
            return c01
        else:
            return c11


def test():

    g1 = [[1, 1],
          [1, 1]]

    g2 = [[1, 1, 1],
          [1, 1, 0],
          [1, 0, 1]]

    g3 = [[1, 1, 1, 1, 1],
          [1, 1, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1]]

    g4 = [[1, 1, 1, 1],
          [1, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 0, 1, 1]]

    g5 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1]]

    g6 = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]

    g7 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]]


    assert not partial_validity_check([0,0], g1)
    assert not partial_validity_check([0,0,1], g2)
    assert partial_validity_check([1,None,None], g2)
    assert partial_validity_check([0,None,None], g2)
    assert partial_validity_check([1,0,0], g2)
    assert partial_validity_check([1,1,0], g2)
    assert partial_validity_check([0,1,None], g2)
    assert not partial_validity_check([0,None,0], g2)
    assert not partial_validity_check([0, 1, 1, 0, 1, 0], g5)
    assert partial_validity_check([0, 1, 1, 1, 0, 0], g5)
    assert partial_validity_check([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1], g6)



    assert vertex_cover_tree(g1) in [[1,0],[0,1]]
    assert vertex_cover_tree(g2)  == [1,0,0]
    assert vertex_cover_tree(g3) in [[1, 0, 1, 0, 1],
                                    [1, 0, 0, 1, 1]]
    assert vertex_cover_tree(g4)  == [1, 0, 1, 0]
    assert vertex_cover_tree(g5)  in  [[0, 1, 1, 1, 0, 0],
                                      [0, 1, 1, 0, 0, 1]]

    assert vertex_cover_tree(g6) in [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                                    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                                    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                                    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                                    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                                    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
                                    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]]

    assert vertex_cover_tree(g7) in [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
start_time = time()
test()
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
