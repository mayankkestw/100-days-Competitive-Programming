"""
Monk and Inversions

Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size  for his birthday. Monk is taking coding classes from Micro. 
They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array.
Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of 
unordered pairs of cells  such that M[i][j]>M[p][q], i<=p and j<=q.
Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.

Input:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.

Output:
Print the answer to each test case in a new line.
"""


def Inversion(matrix):
    c = 0
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if(i<=p and j<=q):
                        if(matrix[i][j]>matrix[p][q]):
                            c+=1
    return c
    
    
T = int(input())
for i in range(T):
    n = int(input())
    matrix = []
    for j in range(n):
        l = [int(x) for x in input().split()]
        matrix.append(l)
    
    result = Inversion(matrix)
    print(result)