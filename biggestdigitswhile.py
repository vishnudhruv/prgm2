n=int(input("Enter a number"))
big=0
while n!=0:
	d=n%10
	if d>big:
		big=d
	n=n//10
print("Biggest digit is  ",big)