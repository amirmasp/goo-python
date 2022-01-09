# A matrix multiplication program

import numpy as np

##**************************************************************************************
# Some healper function to buil the matrix ro and columns
def row(Matrix, r):
    return Matrix[r]
def col(Matrix, c):
    return [v[c] for v in Matrix]
def dot(v1,v2):
    return sum([x*y for x,y in zip(v1,v2)])        

##**************************************************************************************


##**************************************************************************************
def matrix_multi(A,B):
    """
    matrix_multi() function takes two N-dimensional arrays,A and B, and
    performs a matrix multiplication, return a new N-dimensional array.
    We are going to creat a matrix multiplication from ground up.
    this is one-line code answer:
    print(np.matmul(A,B))
    but we will do some hard coding

    """
    A_n = len(A) ## number of rows in matrix A 
    A_m = len(A[0]) ## number of columns in matrix A
    print(' Matrix A\n', A)
    print('A is a',A_n,'x',A_m, 'matrix')
    B_n = len(B) ## number of rows in matrixx B
    B_m = len(B[0]) # number of columns in matrix B
    print('\n Matrix B\n', B)
    print('B is a',B_n,'x',B_m, 'matrix')
    assert A_m == B_n # else throw out an error
    print('A_m =', A_m,', and B_n =', B_n, 'And A_m == B_n is true')

    R_n = A_n
    R_m = B_m
    R = [[0 for j in range(R_m)] for i in range(R_n)] # creating result matrix base on row and column sizes
    print('\nMatrix R(raw)\n', R)
    print('R is a',R_n,'by',R_m, 'matrix')

    for i in range(R_n):
        for j in range(R_m):
            R[i][j] = dot(row(A,i), col(B,j))

    print('\nThe return matrix R (data)\n', R)


    return R


##**************************************************************************************


##**************************************************************************************
def main():
    ## If only want to use np module to matrix multiplication
    #M1 = np.array([[1,-1,2],[0,-2,1]])
    #M2 = np.array([[1,0,1,1],[2,0,1,-1],[3,1,0,2]])
    M1 = [[1,-1,2],[0,-2,1]]
    M2 = [[1,0,1,1],[2,0,1,-1],[3,1,0,2]]
    matrix_multi(M1,M2)


##**************************************************************************************


##**************************************************************************************
if __name__ == '__main__':
    main() 
##**************************************************************************************       