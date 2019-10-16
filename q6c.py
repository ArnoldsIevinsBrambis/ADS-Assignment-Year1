def RMergeSelectionHybrid(listm):										#Functioin for reversed merge sort
	if len(listm) <= 4:													#If lenght of input list is 1 or less, return input list
		listm = RSelectionSort(listm)
		return listm
	middle = int(len(listm)/2)											#Find middle of input list
	left = []															#Define lists left,right,leftsorted,rightsorted
	right = []
	leftsorted = []
	rightsorted = []
	left = listm[0:middle]												#left is left half of input list
	right = listm[middle:len(listm)]									#right is right half of input list
	leftsorted = RMergeSelectionHybrid(left)							#call reversed merge sort recursively on left to sort it and store to leftsorted
	rightsorted = RMergeSelectionHybrid(right)							#call reversed merge sort recursively on right to sort it and store to rightsorted
	return RMerge(leftsorted,rightsorted)								#Return output of merge function for leftsorted and rightsorted

def RMerge(left,right):													#Reversed merge function
	result = []															#Define list result
	while len(left)>0 or len(right)>0:									#While one of, left or right, lists are not empty
		if len(left) > 0 and len(right)>0:								#If both, left and right, lists are not empty
			if left[0] >= right[0]:										#If the first element in left is bigger than or equal to the first element in right
				result.append(left[0])									#Append the first element in left to the result list
				left.remove(left[0])									#And remove the first element in left from left
			else:														#If the first element in right is bigger than or equal to the first element in left
				result.append(right[0])									#Append the first element in right to the result list
				right.remove(right[0])									#And remove the first element in right from right
		if len(left)>0:													#If left is not empty
			result.extend(left)											#Add all elements in left to the result list
			left = []													#And declare left an empty list
		if len(right)>0:												#If right is not empty
			while len(right)>0:											#While right is not empty
				for j in result:										#For the jth element in result
					if right[0] >= j:									#If the first element in right is greater than or equal to the jth element in result
						result.insert(result.index(j), right[0])		#Insert the first element in right in result before the jth element
						right.remove(right[0])							#And remove the first element of right from right
						break											#Break the for loop
					if right[0] < result[len(result)-1]:				#If the first element in right is smaller than the last element of result
						result.append(right[0])							#Add the first element in right to the end of result
						right.remove(right[0])							#And remove the first element of right from right
						break											#Break the for loop
			right = []													#Declare right to be an empty list
	return result														#Return the result list

def RSelectionSort(listm):												#Reversed selection sort function
	for i in range(len(listm)-1,0,-1):									#For i from the lenght of input list minus one to zero stepping in intervals of -1
		elem = 0														#Declare variable for position of largest element in listm
		for j in range(1,i+1):											#For j in range from 1 to i+1 (i.e. to the position up to which the list has been sorted, since it is being sorted right to left)
			if listm[j] < listm[elem]:									#If the jth element is greater than element at position elem
				elem = j												#Set position of elem to position j
		temp = listm[i]													#Temporary value for storing the value of the ith element in listm
		listm[i] = listm[elem]											#Set the ith element in listm to the element at position elem in listm
		listm[elem] = temp												#Set the element at position elem of listm to have the value of temp (effectively swapping listm[i] and listm[elem])
	return listm														#Return listm


print(RMergeSelectionHybrid([1,23,2,3,6543,34,24,15,12,12312312,44,4325]))
# Sorted input takes the most steps to reverse sort for the selection sort algorithm. 
# The main hybrid algorithm will split the input into two halves each time until the size of the input is 4 or less.
# To obtain the worst case for this hybrid algorithm, sorted bacthes of 3 or 4 have to be input in pairs. 
# For example the list (5,6,7,8,1,2,3,4) or (8,9,10,1,2,3,5,6,7,4,11,12). 
