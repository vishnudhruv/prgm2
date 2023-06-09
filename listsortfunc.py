a=[]
n=int(input("Enter the number of elements :"))
print("Enter the elements ")
for i in range(0,n):
	k=int(input())
	a.append(k)
print(a)
a.insert(2,56) # insert 56 into the index 2
print(a)
a.pop(2) # removes an element at index 2, if index is not mentioned, last element is removed
print(a)
del a[3] # removes an element at index 2
print(a)
a,remove(75) # removes 75 from the list
print(a)
a.index(75) # returns the index of first occurence of 75 in the list
b=a.copy() #copied the content of list a into b
print(b)
del a  # delete the list completely
print(a)
a.clear() # empties the list
print(a)  
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)