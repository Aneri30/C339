def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

sort = [5,-8,6,7,-2]
#sort = ["mia", "anna", "kristina", "mike"]
#sort = ['c', 'b', 'd', 'a']

bubble_sort(sort)
print(sort)