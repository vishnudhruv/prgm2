n=int(input("Enter a number : "))
sd=9
while n!=0:
	d=n%10
	if d<sd:
		sd=d
	n=n//10
print("Smallest digit ",sd)


