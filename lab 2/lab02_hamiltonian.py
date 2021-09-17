from itertools import permutations

""" 
      Sabemos que el coste de un bucle for es O(n), por ende, al tener un for anidado dentro de otro
      podemos valorar que el coste de este algoritmo es de O(n²). El resto de operaciones que realizamos son
      comparaciones o asignaciones, las cuales tienen un coste constante.    """

def graph_has_Hamiltonian_circuit(g):
    # g is a conected nondirected graph
    # decides whether g has a Hamiltonian circuit
    # DEVOLVER LAS LISTAS QUE SI SON HAMILTONIANAS
    
      asignaciones = permutations(list(range(len(g))))            # Permutaciones de los distintos grafos
      for valore in asignaciones:                                 # Recorremos cada una de las permutaciones disponibles
            hamiltoniano = True                                   # Utilizamos esta flag para saber cuando alguno de los vertices no son conexos entre si
            for i in range(len(valore)-1,0,-1):                   # Recorremos la permutacion de manera decreciente
                  if(g[valore[i]][valore[i-1]] != 1):             # Comprobamos el vertice actual y el anterior para comprobar si estan conectados
                        hamiltoniano = False                      # En caso de que no lo sean, marcamos la flag como false
            if (g[valore[0]][valore[len(valore)-1]] == 1 and hamiltoniano):   # Comprobamos que el ultimo vertice y el primer tambien son conectos para que sea un ciclo
                  print(valore)                                   # Si esto ocurre, sabemos que es un ciclo hamiltoniano, por lo que printeamos esta permutacion
                  return True                                     # y devolvemos un valor true para el assert
      return False                                                # Solamente llegaremos aqui en caso de recorrer todas las permutaciones y no encontrar un ciclo
                                                                  # hamiltoniano, por lo que devolveremos false para el assert
def test():
    g1 = [[1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1],
          [0, 1, 1, 1, 1]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1]]
    
    assert graph_has_Hamiltonian_circuit(g2)

    g3 = [[1, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1, 1]]
    
    assert graph_has_Hamiltonian_circuit(g3)
    
    g4 = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
    g5 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g5)
    
    g6 = [[1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 1, 1],
          [0, 0, 1, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g6)
    
    g7 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
     
    
    assert not graph_has_Hamiltonian_circuit(g7)    

test()
