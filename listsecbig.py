a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
big=a[0]
for i in range(1,n):
	if a[i]>big:
		big=a[i]
i=0
while (1):
	if a[i]!=big:
		sbig=a[i]
		break
	i+=1
for i in range(i+1,n):
	if a[i]<big and a[i]>sbig:
		sbig=a[i]
print("Biggest : ",big)
print("2nd Biggest : ",sbig)


	