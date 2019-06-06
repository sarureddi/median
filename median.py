num=int(input("enter the value"))
num.sort()
length=len(num)
if(length%2==0):
  median=(num((length)//2)+num((length)//2-1))/2
else
  median=num((length-1)//2)
print(median)
