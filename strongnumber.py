n=int(input("Enter a number"))
temp=n
sum=0
while n!=0:
	d=n%10
	fact=1
	while d>1:
		fact*=d
		d-=1
	sum+=fact
	n=n//10
if sum==temp:
	print("Strong number")
else:
	print("Not a strong number")

