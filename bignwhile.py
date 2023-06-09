n=int(input("Enter the count"))
big=int(input("Enter the numbers"))
i=2
while i<=n:
	no=int(input())
	if no>big:
		big=no
	i+=1
print("Biggest is : ",big)

