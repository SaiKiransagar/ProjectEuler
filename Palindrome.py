"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
x = int(input('Enter number of digits:'))
high=(10**x)-1
low=10**(x-1)
lpn=0

for i in range(high,low+1,-1):
    a=i
    for j in range(i,low+1,-1):
        num=a*j
        if (num < lpn):
            break
        temp=num
        rev=0
        while (num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10

        if (temp==rev and temp>lpn):
            print(a)
            print(j)
            lpn=temp
            

print(lpn)











