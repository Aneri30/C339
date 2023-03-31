def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    #choose the pivot element
    pivot = arr[0]

    #Partition the array in two sub arrays
    lesser =[i for i in arr[1:] if i<=pivot] 
    right =[i for i in arr[1:] if i > pivot]

    return quicksort(lesser)+[pivot]+quicksort(right)
    
quicksort([27,14,35,10,19])