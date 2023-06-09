a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
for i in range(0,n//2):
	if a[i]!=a[n-i-1]:
		print("List is not symmetric ")
		break
else:
	print("List is symmetric ")
