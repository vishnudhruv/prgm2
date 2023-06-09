a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
for i in range(0,n-1):
	for j in range(0,n-i-1):
		if a[j]>a[j+1]:
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
print("List elements are : ")
for i in range(0,n):
	print(a[i])

