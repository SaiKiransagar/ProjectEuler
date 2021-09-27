"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=[]


for i in range(2,max(a)):
    for j in range(2,i):
        if i%j==0:
            break
    else:

        b.append(i)





def code(z):
    global a
    global x
    x=0
    global mul
    mul=1
    while x==0:
        x=1
        for i in range(0,len(a)):
            if a[int(i)]%z==0:
                x=0
                a[int(i)]=a[int(i)]/z
        if x==0:
            mul*=z
    return mul

result=1
for i in b:
    if i!=1:
        result*=code(i)
  
    
print(result)
