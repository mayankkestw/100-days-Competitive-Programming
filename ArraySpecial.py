def findSpecialProduct(inputArray):
    i, temp = 1, 1
    n = len(inputArray)
    prod = [1 for i in range(n)] 
  
  
    for i in range(n): 
        prod[i] = temp 
        temp *= arr[i] 
  
    temp = 1
  
    for i in range(n - 1, -1, -1): 
        prod[i] *= temp 
        temp *= arr[i] 

  
    return prod

if __name__ == '__main__':
    

    inputArray_count = int(input().strip())

    inputArray = []

    for _ in range(inputArray_count):
        inputArray_item = int(input().strip())
        inputArray.append(inputArray_item)

    result = findSpecialProduct(inputArray)