def hash_quadratic(d):								
	table = ["-"]*19							#create array of size 19
	for k in d:									#for the kth element in input array
		if k in table:							#if this element is already in the result array, go to next input element
			continue
		hashFirst = (6*k+3) % 19				#initial hash function
		i = hashFirst							#store the result to variable i
		if table[i] == "-":						#check if ith slot in result array is empty
			table[i] = k						#if it is, store input element k to it
		else:									#if not
			for n in range(0,20):				
				i=((n*n)+ hashFirst)%19			#do quadratic probing using the first hash function result and n<=19, store the result to i
				if k in table:					#if this element is already in the result array, go to next input element
					continue
				else:
					if table[i] == "-":			#check if ith slot in the result array is empty
						table[i] = k			#if it is, store input element k to it
	return table								#return the result array
				
def hash_double(d):
	table = ["-"]*19									#create array of size 19
	for k in d:											#for the kth element in input array
		if k in table:									#if this element is already in the result array, go to next input element
			continue
		hashFirst = ((6*k)+3)%19						#initial hash function
		if table[hashFirst] == "-":						#check if hashFirst(first hash function result) slot in result array is empty
			table[hashFirst] = k						#if it is, store input element k to it
		else:											#if not
			for j in range(0,20):						
				hashSecond = 11 - (k%11)				#calculate hashSecond value needed for double hashing
				i =(hashFirst + (j*hashSecond))%19		#do double hashing using the result from the first function, hashSecond value and j<=19, store result to i
				if table[i] == "-":						#check if ith slot in the result array is empty
					table[i] = k						#if it is, store input element k to it
					break								#exit the for loop
	return table										#return the result array
