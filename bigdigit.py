n=int(input("Enter a number : "))
bd=0
while n!=0:
	d=n%10
	if d>bd:
		bd=d
	n=n//10
print("greatest digit ",bd)