n=int(input("Enter a number : "))
f=1
for i in range(n,1,-1):
	f=f*i
	print(i,end="x");
print("1=",f)
