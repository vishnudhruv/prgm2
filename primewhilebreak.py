n=int(input("Enter a number"))
i=2
while i<n:
	if n%i==0:
		print(n," is composite")
		break
	i=i+1
else:
	print(n," is prime")


