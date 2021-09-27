""""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

limit=int(input('Enter a Numbr:'))

sum=0
for i in range (1,limit):
    if i%3 ==0 or i%5==0:
        sum+=i

print(sum)



#2nd Method runs faster
limit=int(input('Enter a Numbr:'))
firstfactor = int(input('Enter 1st factor:'))
secondfactor = int(input('Enter 2nd factor:'))
sum=0

x = (limit-1)//firstfactor
y = (x*(x+1)*(firstfactor))/2
sum=sum+y

x = (limit-1)//secondfactor
y = (x*(x+1)*(secondfactor))/2
sum=sum+y

x = (limit-1)//(firstfactor*secondfactor)
y = (x*(x+1)*(firstfactor*secondfactor))/2
sum=sum-y

print(sum)















