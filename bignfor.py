n=int(input("Enter the count"))
big=int(input("Enter the numbers"))
for i in range(1,n):
	no=int(input())
	if no>big:
		big=no
print("Biggest is : ",big)