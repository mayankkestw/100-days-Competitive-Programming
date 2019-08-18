'''
Coders here is a simple task for you, you have given an array of size N and an integer M.
Your task is to calculate the difference between maximum sum and minimum sum of N-M elements of the given array.
'''

def diff(arr, l):
    size = l[0] - l[1]
    
    arr = sorted(arr)
    
    d1 = sum(arr[:size])
    d2 = sum(arr[-size:])
    
    d = d2-d1
    
    return d
    
    
    
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        l = list(map(int, input().rstrip().split()))
        arr = list(map(int, input().rstrip().split()))
        difference = diff(arr=arr, l=l)
        print(difference)