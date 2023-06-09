n=int(input("Enter a number : "))
s=sum(int(i) for i in str(n))
print("Single digit sum = ",s%9 if s%9 else 9)