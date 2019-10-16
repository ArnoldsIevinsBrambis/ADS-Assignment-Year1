def count_ephemeral(n1, n2, k):					#Main function for counting the number of ephemerals in the specified range
	global eternal								#Declares global variable to be used when determining whether a k-descendant sequence is eternal
	global KDS									#Declares global variable to be used to store information about whether a numbers k descendant
	KDS = {1:True}								#Set true value for 1 (true for ephemeral)
	ephemeralCount = 0							#Declares variable for counting number of ephemeral numbers in range
	for i in range(n1,n2):						#For every value in the specified range
		eternal = []							#Reset the eternal variable to an empty list (to create a new list for every number)
		if findKDS(i,k) == True:				#If the number produces a k-ephemeral k-descendant sequence add 1 to the count of k-ephemeral numbers 
			ephemeralCount += 1					
	return ephemeralCount						#Output the number of k-ephemeral numbers 

def kchild(n, k):								#Function for calculating the kchild of a number given the number and k
	kchild = 0									#Declares the kchild variable
	numbers = [int(i) for i in str(n)]			#Splits the number into a list of digits
	for g in numbers:							#For each digit in the list
		kchild += g**k							#Add that digit to the power of k to the kchild variable
	return kchild								#Output the kchild value of the number

def findKDS(n,k):								#Function for determining whether a number is k-ephemeral
	global KDS									#Declares global variable to be used when determining whether a k-descendant sequence is eternal
	global eternal								#Declares global variable to be used to store information about whether a numbers k descendant
	if n in eternal:							#If this number has alrady been called in this instance of finding a k-descendant dequence, its k-descendant sequence is eternal
		KDS[n] = False							#Declare the k-descendant sequence of this number to be eternal in the KDS dictionary
	if n not in KDS:							#If this number does not have a value in the k-descendant sequence dictionary
		# ~ if n == 1:
			# ~ KDS[n] = true
		# ~ else:
		eternal.append(n)						#Append this number to the eternal list so its k-descendant sequence can be deemed eternal if it repeats
		KDS[n] = findKDS(kchild(n,k),k)			#Recursively call the findKDS function to determine if the given numbers k-descendant sequence is ephemeral by inputing its kchild into the function with the same k value.
	return KDS[n]								#Output the boolean for the k-descendant sequence of this number (true for ephemeral, false for eternal.
