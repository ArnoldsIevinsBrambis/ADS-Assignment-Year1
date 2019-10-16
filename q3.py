
#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

#####################################################

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after
    
   
#####################################################
def testq3():
    assert good_expression("1+2+3+4")
    print("Test 1")
    assert not good_expression("(1+2+3+4)")
    print("Test 2")
    assert good_expression("(1+2)*3+4")
    print("Test 3")
    assert not good_expression("((1+2))*3+4")
    print("Test 4")
    assert good_expression("1+2*3+4")
    print("Test 5")
    assert not good_expression("1+(2*3)+4")
    print("Test 6")
    assert good_expression("1*2+3+4")
    print("Test 7")
    assert not good_expression("1*2+(3+4)")
    print("Test 8")
    assert good_expression("(1+2*3*((4+5)*6+7)+8)*9")
    print("Test 9")
    assert not good_expression("((1+2))*3+4")
    print("Test 10")
    assert not good_expression("1+(2*3)+4")
    print("Test 11")
    assert not good_expression("1*2+(3+4)")
    print("Test 12")
    assert good_expression("(1+2)*3+4")
    print("Test 13")
    assert good_expression("1+2*3+4")
    print("Test 14")
    assert good_expression("1*2+3+4")
    assert good_expression("1+(2+3)*(4+5)")
    print ("all tests passed")
#####################################################																	#Above code is provided as part of the assignment.
def find_brackets(aape):																								#Secondary function - removes brackets and replaces them with P for valid brackets and R for invalid brackets.
	aape = aape
	global s
	global sapes
	if "((" in sapes:
		doublebrackets = True
	else:
		doublebrackets = False
	s = Stack()
	t = 0
	o = 0
	plus = []
	times = []
	listcalledstack = []
	occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
	while "(" in aape:															#While open brackets symbol is in the input list, replaces brackets with P or R respectively.
		brackets = list(occurrences("(", aape))
		for i in aape:
			if i in "(+":
				listcalledstack.append(i)
				if i == "(":
					s.push(i)
					t = aape.index(i)
			if i == ")":
				h = listcalledstack.pop()
				o = aape.index(i)
				if h == "+":
					while True:
						if len(listcalledstack) == 0:
							break
						g = listcalledstack.pop()
						if g == "(":
							break
					aape[t] = "P"
					if doublebrackets == True:
						t = brackets.pop()
					del aape[t+1:o+1]
					break
				if h == "(":
					aape[t] = "R"
					del aape[t+1:o+1]
					break
	while ")" in aape:															#While close brackets symbol is in the input list, replaces brackets with P or R respectively.
		for i in aape:
			if i in "P+*":
				if i == "P":
					t = aape.index(i)
				if i == "+":
					plus.append(i)
				if i == "*":
					times.append(i)
			if i == ")":
				o = aape.index(i)
				if len(times) == 0:
					aape.append("R")
					break
				else:
					aape[t] = "P"
					del aape[t+1:o+1]
					break
	return aape

def good_expression(sape):														#Main function - determines whether the provided expression is valid.
	global sapes
	sapes = sape
	li = [str(i) for i in str(sape)]
	g = []
	seek = find_brackets(li)
	print(seek)
	verdict = False

	if "R" in seek:																#If the find_brackets function has found redundant brackets, return false.
		verdict = False
		return verdict
	if "P" in seek:
		occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
		g = list(occurrences("P", seek))
		for i in g:																#If there is no times simbol to the left or right of a valid set of brackets(one that holds addition) in the input, return false.
			if i != 0:
				left = i-1
				right = i+1
				if seek[left] != "*":
					if right > len(seek)-1:
						verdict = False
						return verdict
					if seek[right] != "*":
						if seek[left] == "+":
							verdict = False
							return verdict
						if seek[right] == "+":
							verdict = False
							return verdict
		if "*" not in seek:														#If there was a set of brackets in the input, but no multiplication, return false.
			verdict = False
			return verdict
		
	if "(" not in li:															#If there were no brackets in the input, return true.
		if ")" not in li:
			verdict = True
			return verdict
	if "*" in seek:
		if "P" in seek:
			str1 = ''.join(str(e) for e in seek)
			print(str1)
			verdict = match(str1)
	return verdict
	
def match(string):																#Function for matching pairs of brackets.
    left, right, pairs = "({[", ")}]", ["()", "{}", "[]"]
    global s
    s = Stack()
    judgement = True
    for char in string:
        if char in left:
            s.push(char)
        if char in right:
            if s.isEmpty() == True:
                judgement = False
                return	judgement
            char2 = s.pop()
            if char2 + char not in pairs:
                judgement = False
                return	judgement
    if s.isEmpty() == False:
        judgement = False
        return
    judegement = True
    return 	judgement
testq3()
