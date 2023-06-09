n=int(input("Enter a number"))
sum=0
product=1
while n!=0:
	d=n%10
	sum+=d
	product*=d
	n=n//10
if sum==product:
	print("Spy Number")
else:
	print("Not a spy number")

