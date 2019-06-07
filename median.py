num1=[1,2,3,4,5]
num1.sort()
length=len(num1)
if(length%2==0):
  median=(num1((length)//2)+num1((length)//2-1))/2
else:
  median=num1((length-1)//2)
print(median)
