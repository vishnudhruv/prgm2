a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
no=int(input("Enter the element to count : "))
count=0
for i in range(0,n):
	if a[i]==no:
		count+=1
if count==0:
	print(no," not in the list")
else:
	print(no," occured ",count," times")