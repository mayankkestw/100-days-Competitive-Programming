#include <iostream>
using namespace std;
  
void swap(int* x, int* y) 
{ 
    int temp = *x; 
    *x = *y; 
    *y = temp; 
} 
  
int partition (int array[], int low, int high) 
{ 
    //Pivot element selected as right most element in array each time.
    int pivot = array[high];    
    int swapIndex  = (low - 1);   //swapping index.
  
    for (int j = low; j <= high- 1; j++) 
    { 
        //Check if current element is smaller than pivot element.
        if (array[j] < pivot) 
        { 
            swapIndex ++;    //increment swapping index.
            swap(&array[swapIndex], &array[j]); 
        } 
    } 
    swap(&array[swapIndex + 1], &array[high]); 
    return (swapIndex + 1); 
} 
  
       /* indexPI is partitioning index, partition() function will 
        return index of partition */
        int indexPI  = partition(array, low, high); 
  
        quickSort(array, low, indexPI  - 1);  //left partition
        quickSort(array, indexPI  + 1, high); //right partition
    } 
} 
  
} 
  
    quickSort(array, 0, size-1); 
    cout<<"After Sorting: \n"; 
    display(array, size); 
    return 0; 
}
