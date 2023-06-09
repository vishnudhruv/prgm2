n=int(input("Enter the count : "))
e=2
s=0
for i in range(n,0,-1):
	s+=e
	e+=2
print("Sum is ",s)

