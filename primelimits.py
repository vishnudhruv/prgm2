l=int(input("Enter the lower limit : "))
u=int(input("Enter the upper limit : "))
for i in range(l,u+1):
	if l==1:
		continue
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i)