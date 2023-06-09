a=[]
n= int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	k=int(input())
	a.append(k)
count=0
ele=int(input("Enter the element to count : "))
for x in a:
	if x==ele:
		count+=1
print(ele," occured ",count," times")



