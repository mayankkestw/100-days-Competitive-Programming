'''
Monk and Welcome Problem

Having a good previous year, Monk is back to teach algorithms and data structures. This year he welcomes the learners with a problem which he calls "Welcome Problem". The problem gives you two arrays A and B (each array of size N) and asks to print new array C.
Now, Monk will proceed further when you solve this one. So, go on and solve it :)

Input:
First line consists of an integer N, denoting the size of A and B.
Next line consists of N space separated integers denoting the array A.
Next line consists of N space separated integers denoting the array B.

Output:
Print N space separated integers denoting the array C.
'''

def addArray(A,B):
    C = [x+y for x,y in zip(A,B)]
    return C
    

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
    
result = addArray(A, B)

print(*result, sep=" ")