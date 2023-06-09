n=int(input("Enter a number"))
small=9
while n!=0:
	d=n%10
	if d<small:
		small=d
	n=n//10
print("Smallest digit is  ",small)






