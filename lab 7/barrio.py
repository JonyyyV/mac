from time import time


def evaluate_clause(clausula, A):
    for literal in clausula:
        if (A[abs(literal)] != None) and ((literal > 0) == A[abs(literal)]):
            return True
    else:
        return False

def evaluate_formula(clauses, A):
    respuesta=True
    for clausula in clauses:
        respuesta= respuesta and evaluate_clause(clausula,A)
        if not respuesta:
            return False
    else:
        return True

def sat_preprocessing(num_variables, clausulas, asignation=None):
    clauses=[None]*len(clausulas)
    for i in range(len(clausulas)):
        clauses[i]=list(clausulas[i])
    
    if not asignation:
        A = [None]*(num_variables+1)
        A[0] = 0
    else:
        A = list(asignation)

    cambios=True
    while cambios:
        if len(clausulas)==0:
            return []
        

        aparaciones= [0]*(num_variables+1)

        cambios=False
        
        for i in clauses:
            for literal in i:
                aparaciones[abs(literal)] += 1

            if len(i) == 1 and A[abs(i[0])]==None:
                if i[0]<0:
                    A[-i[0]]=0
                else:
                    A[i[0]]=1  
        
        for h in range(num_variables+1):
            if aparaciones[h]==1 and A[h]==None:
                for i in clauses:
                    if h in i:
                        A[h]=1
                    elif -h in i:
                        A[h]=0
        
        for i in range(len(clauses),0,-1):
            clausula=clauses[i-1]
            if evaluate_clause(clausula, A):
                clauses.pop(i-1)

                if not cambios:
                    cambios=True
        
        for i in range(len(clauses),0,-1):
            clausula=clauses[i-1]
            for j in range(len(clausula),0,-1):
                literal= clausula[j-1]
                if(A[abs(literal)] != None):
                    if ((literal > 0) != A[abs(literal)]):
                        clausula.pop(j-1)
        
                        if not cambios:
                            cambios = True

        if clauses.count([]) > 0:
            return ([[1],[-1]], None)
        elif evaluate_formula(clauses, A):
            return ([], A)
        elif not cambios:
            return (clauses, A)

 
if __name__=="__main__":
    def test():
        assert [] == sat_preprocessing(1, [[1]])[0]
        assert [[1],[-1]] == sat_preprocessing(1, [[1], [-1]])[0]
        assert [] == sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                             [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                             [1, 3, -4], [3, -4, 1], [-1]])[0]
        assert [[1],[-1]] == sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                             [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                             [-3, -1], [-4], [4, -1, 2]])[0]
        ans = [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
        assert ans == sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                            [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                            [-1, -5, 2, 3], [-3, 2, -5, 6, -4]])[0]
        # Nuevo assert
        assert [] == sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                            [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                            [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]])[0]
             
    
    start_time = time()
    test()
    elapsed_time = time() - start_time
    print("Elapsed time: {:10f}".format(elapsed_time))