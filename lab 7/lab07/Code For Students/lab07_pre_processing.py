 
def sat_preprocessing(num_variables, clauses, assignment):
    list_clauses = list(clauses)
    if not assignment:
        list_assignment = [None] * (num_variables + 1)
        list_assignment[0] = 0
    else:
        list_assignment = list(assignment)

    update = True
    while update:  
        # TODO
        if not (len(clauses)):
            return []      

        check = [0] * (num_variables + 1)
        update == False

        for i in list_clauses:
            for j in i:
                check[abs(j)] += 1
                
                if len(i) == 1 and list_assignment[abs(i[0])] == None:
                    if i[0] < 0:
                        list_assignment[-i[0]] = 0
                    else:
                        list_assignment[i[0]] = 1
            
            for i in range(num_variables + 1):
                if list_assignment[i] == None and check[i] == 1:
                    for j in list_clauses:
                        if j in i:
                            check[i] = 1
                        elif -i in j:
                            check[i] = 0
            
            for i in range(len(clauses),0,-1):
                clauses_aux = list_clauses[i - 1]
                for j in range(len(clauses_aux,0,-1)):
                    aux = clauses_aux[j-1]
                    if(list_assignment[abs(aux)] != None):
                        if((aux > 0) != list_assignment(abs(aux))):
                            clauses_aux.pop(j-1)

                            if not update:
                                update = True

        if [] in clauses:
            return ([[1], [-1]], assignment)
        else:
            if (clauses == []) or (not update):
                     return (clauses, assignment)  

    

def test():
    assert ([], [None, 1]) == sat_preprocessing(1, [[1]], [None, None])
    
    
    assert ([[1],[-1]]) == sat_preprocessing(1, [[1], [-1]], [None,None])[0]
    
    
    ans = sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                         [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                         [1, 3, -4], [3, -4, 1], [-1]], [None, None, None, None, None])
    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][2] == 1
    assert ans[1][4] == 1
    
    
    ans = sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                [-3, -1], [-4], [4, -1, 2]], 
                                  [None, None, None, None, None, None])
    assert ans[0] == [[1],[-1]]            
    
    
    ans = sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4]], 
                                   [None, None, None, None, None, None, None])
    assert ans[0] == [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans[1][1] == 1
    
    
    ans = sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]], 
                                   [None, None, None, None, None, None, None, None] )
    assert ans[0] == []
    assert ans[1][1] == 1
    assert ans[1][4] == 1
    assert ans[1][6] == 1
    assert ans[1][7] == 1
    
   
    ans = sat_preprocessing(6, [[-6, -4, 5, -1, ], [1,2,3,6,-5],
                                [4,6], [-4, -3], [-1],
                                [1,6,-5,-4], [3,5,-6,-5,-1]],
                                   [None, None, None, None, None, None, None])
    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][2] == 1
    assert ans[1][3] == 0
    assert ans[1][5] == 0
    assert ans[1][6] == 1   
   
test()
