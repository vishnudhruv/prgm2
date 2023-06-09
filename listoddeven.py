a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
print("List elements are : ")
for i in range(0,n):
	print(a[i])
odd=[]
even=[]
for i in range(0,n):
	if a[i]%2==0:
		even.append(a[i])
	else:
		odd.append(a[i])
print("EVEN LIST")
for x in even:
	print(x)
print("ODD LIST")
for x in odd:
	print(x)




