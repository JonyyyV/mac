from time import time

# cover es una lista de 0s, 1s y Nones.
# Si i es la posicion de un 1, el i-esimo nodo esta en el cover.
# Si i es la posicion de un 0, el i-esimo nodo no esta en el cover.
# Si i es la posicion de un None, no sabemos si el i-esimo nodo estara en el cover.
#
# partial_validity_check comprueba, dado un posible cover y un grafo,
# si los nodos del cover pueden llegar a cubirir todas las aristas del grafo o no.


def partial_validity_check(cover, graph):
    # TODO: Programa el codigo de la funcion

    for i in range(len(graph)):                                         # Recorremos con ambos for's la totalidad del grafo
          for j in range(len(graph)):
              if j!=i:                                                  # En las posiciones en las que i y j no sean iguales, ya que es el mismo nodo
                  if graph[i][j]==1 and cover[i]==0 and cover[j]==0:    # En caso de que esa posicion tenga un 1 y ambos cover's sean igual a 0
                      return False                                      # devolvemos False, por lo que dejamos de buscar
    return True                                                         # En caso de que lleguemos a este punto del codigo, sabremos que debemos devolver un True
       

# vertex_cover_tree inicializa y llama al arbol de busqueda
def vertex_cover_tree(graph):
    n = len(graph)
    cover = [None]*n
    return recursive_vertex_cover(graph, cover)




# recursive_vertex_cover construye recursivamente el arbol de busqueda 
def recursive_vertex_cover(graph, cover):

    ############
    # TODO: Programa esta parte de la funcion
    #
    # Comprueba es posible construir un cover valido.
    # Si no es posible, devuelve [1]*len(cover).
    # En otro caso, 
    # si el cover esta completo, lo devuelve.
    # Si esta incompleto, encuentra un nodo v que no esta en el cover.
    
    
    # Final de tu codigo
    # Lo siguiente abre las dos ramas del arbol de busqueda.
    # No modificar nada.
    ##############
    if not partial_validity_check(cover, graph):    # Adecuandonos a los requisitos del codigo, en caso de que no sea capaz construir un cover,
        return [1]*len(cover)                       # devolvemos [1]*len(cover)
    else:                                           # En el caso de que el cover se pueda construir
        v=-101                                      # Creamos una bandera, inicializada a un numero que no es posible que salga como resultado del cover
        for i in range(len(cover)):                 # Recorremos todos los nodos del cover
            if cover[i] == None:                    # En caso de que algun nodo del cover este vacio
                v = i                               # guardamos la posicion del mismo, para tratarlo a posteriori
                break                               # Tras esto, podemos terminar el bucle
        if v==-101:                                 # En caso de que lleguemos aqui con ese valor, significa que el cover se encuentra completo
            return cover                            # Por lo que devolvemos el cover inicial

        copy_cover = list(cover)                    
        cover[v] = 0
        c0 = recursive_vertex_cover(graph, cover)
        cover = list(copy_cover)
        cover[v] = 1
        c1 = recursive_vertex_cover(graph, cover)
        return c0 if c0.count(1) < c1.count(1) else c1

        
def test():
    
    g1 =  [[1, 1],
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
