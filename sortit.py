'''
Sort it Out

You are given an array A of non-negative integers of size m. Your task is to sort the array in non-decreasing order and print out the original indices of the new sorted array.

Example:

A={4,5,3,7,1}

After sorting the new array becomes A={1,3,4,5,7}.

The required output should be "4 2 0 1 3"   

'''

def SortItOut(arr, n):
    l = [0]*n
    arr2 = sorted(arr)
    for i, j in enumerate(arr):
        for k, m in enumerate(arr2):
            if j==m:
                l[k] = i
    return l
    
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    l = SortItOut(arr, n)
    print(*l, sep=" ")