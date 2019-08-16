"""
Monk and Rotation
Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

Input:
The first line will consists of one integer T denoting the number of test cases. 
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.
Output:
Print the required array.

"""

from collections import deque

def rotate(arr, steps):
    d = deque(arr)
    d.rotate(steps)
    result = list(d)
    return result
    
    
T = int(input())
for i in range(T):
    N, K = input().split()
    N, K = int(N), int(K)
    arr = [int(i) for i in input().split()]
    result = rotate(arr=arr, steps=K)
    print(*result, sep=" ")
    
'''    
def right_rotation(a, k):
   # if the size of k > len(a), rotate only necessary with
   # module of the division
   rotations = k % len(a)
   return a[-rotations:] + a[:-rotations]
    
T = int(input())
for i in range(T):
    N, K = input().split()
    N, K = int(N), int(K)
    arr = [int(i) for i in input().split()]
    result = right_rotation(arr, K)
    print(*result, sep=" ")
'''