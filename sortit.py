'''
Sort it Out

You are given an array A of non-negative integers of size m. Your task is to sort the array in non-decreasing order and print out the original indices of the new sorted array.

Example:

A={4,5,3,7,1}

After sorting the new array becomes A={1,3,4,5,7}.

The required output should be "4 2 0 1 3"   

'''

def SortItOut(arr):
    n = len(arr)
    indices = list(range(n))
    
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                indices[j], indices[j+1] = indices[j+1], indices[j]
                swapped = True
        if not swapped:
            break

    return indices
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    l = SortItOut(arr)
    print(*l, sep=" ")