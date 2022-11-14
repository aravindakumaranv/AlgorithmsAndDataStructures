def merge(left, right):
	arr = []
	i = 0
	j = 0
	while i<len(left) and j<len(right):
		if(left[i]<=right[j]):
			arr.append(left[i])
			i+=1
		else:
			arr.append(right[j])
			j+=1
	while(i<len(left)):
		arr.append(left[i])
		i+=1
	while(j<len(right)):
		arr.append(right[j])
		j+=1
	return arr

def mergeSort(arr):
	if(len(arr)==1):
		return arr
	left = arr[0:len(arr)//2]
	right = arr[len(arr)//2:len(arr)]
	left = mergeSort(left)
	right = mergeSort(right)
	arr = merge(left, right)
	return arr

def insertionSort(arr):
	for j in range(1,len(arr)):
		n = arr[j]
		i = j-1
		while (i>=0 and arr[i]>n):
			arr[i+1] = arr[i]
			i = i-1
		arr[i+1] = n
	return arr

def selectionSort(arr):
	n = len(arr)
	for j in range(n):
		iMin = j
		for i in range(j+1,n):
			if(arr[i] < arr[iMin]):
				iMin = i
		if(iMin != j):
			temp = arr[j]
			arr[j] = arr[iMin]
			arr[iMin] = temp
	return arr

def bubbleSort(arr):
	n = len(arr)
	for i in range(1,n):
		for j in range(1,n-i+1):
			if(arr[j-1]>arr[j]):
				temp = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp
	return arr

def binarySearch(arr, x):
	mid = len(arr)//2
	if(arr[mid] == x):
		return mid
	if(x >= arr[mid]):
		binarySearch(arr[mid:],x)
	else:
		binarySearch(arr[0:mid],x)
	return -1

arr = [3,2,5,4,3,1,0]
print(mergeSort(arr))

