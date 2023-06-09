a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
no=int(input("Enter the sum : "))
for i in range(0,n-1):
	for j in range(i+1,n):
		if a[i]+a[j]==no:
			print(a[i],"-",a[j])

