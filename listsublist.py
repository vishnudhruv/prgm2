a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
b=[]
m= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,m):
	k=int(input())
	b.append(k)
for i in range(0,n-m+1):
	if a[i:i+m]==b:
		print("Yes exists")
		break
else:
	print("No do not")



