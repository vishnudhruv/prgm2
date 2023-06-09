a=[]
n=int(input("Enter the number of elements : "))
for i in range(0,n):
	k=int(input())
	a.append(k)
b=set(a)
a=list(b)
print(a)