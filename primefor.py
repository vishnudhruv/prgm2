n=int(input("Enter a number : "))
if n!=1:
	for i in range(2,n):
		if n%i==0:
			print(n,"is composite")
			break
	else:
		print(n," is prime")
else:
	print("Neither prime nor composite ")

