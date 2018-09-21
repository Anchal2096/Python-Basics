import math
def heapify(arr,n,i):
     
    largest = i
    left = (2*i)+1
    right = left + 1
    if left < n and arr[largest] < arr[left] :
        largest = left
    if right < n and arr[largest] < arr[right] :
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


def heapsort(arr):
    n = len(arr)
    for i in range(math.floor(n/2)-1,-1,-1):
        heapify(arr,n,i)
    for i in range (n-1, 0, -1):
        arr[0],arr[i] = arr[i], arr[0]
        heapify(arr,i,0)

arr = []
n =int(input("the size of the list"))
for i in range(0,n):
	arr.append(input("enter the values"))

print("the values entered by the user are :")
for i in range (0,n):
	print(arr[i])

heapsort(arr)

print ("the sorted array is")
for i in range (0,len(arr)):
	print (arr[i] ,
end = " ")
