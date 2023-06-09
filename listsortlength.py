list1=["ruby","Python","Java","C"]
for i in range(0,len(list1)-1):
	for j in range(i+1,len(list1)):
		if len(list1[i])<len(list1[j]):
			temp=list1[i]
			list1[i]=list1[j]
			list1[j]=temp;
print("Sorted list based on length ")
for i in list1:
	print(i)
