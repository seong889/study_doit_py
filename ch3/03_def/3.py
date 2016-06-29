def factorial(a):
	if a is 0 :
		return 1
	return a *factorial(a-1)
	
print("factorial of 7 is", factorial(7))