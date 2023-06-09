n=int(input("Enter the count : "))
s=0
print("Enter the nunbers : ")
for i in range(1,n+1):
	no=int(input())
	if(no%2==0):
		s=s+no
print("Sum of even numbers is : ",s)