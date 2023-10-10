# Python3 Program to DFA that accepts string ending 
# with 01 or 10. 

def q1(s, i) : 

	print("q1->", end=""); 

	if (i == len(s)) : 
		print("NO"); 
		return; 

	# state transitions 
	# 0 takes to q1, 1 takes to q3 
	if (s[i] == '0') :
		q1(s, i + 1); 
	else :
		q3(s, i + 1); 

def q2(s, i) : 

	print("q2->", end = ""); 
	if (i == len(s)) :
		print("NO"); 
		return; 

	# state transitions 
	# 0 takes to q4, 1 takes to q2 
	if (s[i] == '0') :
		q4(s, i + 1); 
	else :
		q2(s, i + 1); 

def q3(s, i) : 

	print("q3->", end = ""); 
	if (i == len(s)) : 
		print("YES"); 
		return; 

	# state transitions 
	# 0 takes to q4, 1 takes to q2 
	if (s[i] == '0') :
		q4(s, i + 1); 
	else :
		q2(s, i + 1); 

def q4(s, i) : 

	print("q4->", end = ""); 
	if (i == len(s)) : 
		print("YES"); 
		return; 

	# state transitions 
	# 0 takes to q1, 1 takes to q3 
	if (s[i] == '0') :
		q1(s, i + 1); 
	else :
		q3(s, i + 1); 

def q0( s, i) : 
	
	print("q0->", end = ""); 
	if (i == len(s)) : 
		print("NO"); 
		return; 

	# state transitions 
	# 0 takes to q1, 1 takes to q2 
	if (s[i] == '0') :
		q1(s, i + 1); 
	else :
		q2(s, i + 1);

# Driver Code 
if __name__ == "__main__" : 
	s = "010101"; 
	
	# all state transitions are printed. 
	# if string is accpetable, YES is printed. 
	# else NO is printed 
	print("State transitions are", end = " "); 
	q0(s, 0); 

# This code is contributed by AnkitRai01
