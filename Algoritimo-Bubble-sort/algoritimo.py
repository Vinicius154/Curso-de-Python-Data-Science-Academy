def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def input_values():
    arr = []
    n = int(input("Quantos números você quer ordenar? "))
    
    for i in range(n):
        num = int(input(f"Digite o número {i+1}: "))
        arr.append(num)
        
    return arr

arr = input_values()
print("Array antes da ordenação:", arr)

bubble_sort(arr)
print("Array ordenado:", arr)