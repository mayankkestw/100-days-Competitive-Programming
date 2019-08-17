"""
Bubble Sort
"""

def BubbleSort(arr):
    N = len(arr)
    for i in range(0, N):
        for j in range(0, N-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
    
if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    
    result = BubbleSort(arr)
    
    print(*result, sep=" ")

