a=[]
n=int(input("Enter no of elements : "))
print("Enter the elements : ")
for i in range(0,n):
	elmnt=int(input())
	a.append(elmnt)
print(a)
b=[a[n-1]]+a[:n-1]
a=b
print(a)