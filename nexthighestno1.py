no=input("Enter a number : ")
l=len(no)
i=l-1
while i>0:
	if no[i-1]<no[i]:
		d1=i-1
		break
	i-=1
if i==0:
	print("No highest number : ")
else:
	i=l-1
	while i>d1:
		if no[i]>no[d1]:
				small=no[i]
				d2=i
				break			
		i-=1
	no=no[:d1]+no[d2]+no[d1+1:d2]+no[d1]+no[d2+1:]
	for i in range(d1+1,l-1):
		for j in range(i+1,l):
			if no[i]>no[j]:
				no=no[:i]+no[j]+no[i+1:j]+no[i]+no[j+1:]
	print("Next Highest number is ",no)
	
	
	







		
