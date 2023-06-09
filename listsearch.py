a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
no=int(input("Enter the element to search : "))
for i in range(0,n):
	if a[i]==no:
		print(no,"found at",i,"index")
		break
else:
	print(no,"not in the list")
