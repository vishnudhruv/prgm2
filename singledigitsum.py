# Program to find the sum of digits of a given number until sum becomes a single digit number

num=int(input("Enter the number : "))	#read the input from user
sum=0							# initialised sum with 0 
while num!=0:						#loop to extract digit and add to sum
	digit=num%10
	sum=sum+digit
	num=num//10
	if num==0 and sum>9:				# to check whether the sum is single digit or not
		num=sum
		sum=0
print("Sum is ",sum )
		
	