no=input("Enter a number : ")
l=len(no)
if l==1:
	print("No higher number ")
else:
	i=l-2
	while i>=0:
		if no[i]<no[i+1]:
			no=int(no[:i]+no[i+1]+no[i]+no[i+2:])
			print(no)
			break
		else:
			no=no[:i]+no[i+1]+no[i]+no[i+2:]
			#i=i+1
		i=i-1
			#no[i+1]=t
			#no=no[:i]+no[i+1]+no[i]
	else:
		print("its the highest no")





		
