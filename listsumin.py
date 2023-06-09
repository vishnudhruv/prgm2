a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
s=0
for x in a:
	s=s+x
print("sum is : ",s)


