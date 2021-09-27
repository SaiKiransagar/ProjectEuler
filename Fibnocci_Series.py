"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

#approach 1) Calcukating sum of all the numbers till 4M and seeing even values and adding

a=1
b=2
sum=2
c=0
limit = 4000000

while c<limit:
    c=a+b
    a,b=b,c
    if c%2 ==0:
        sum+=c

print(sum)



#approach 2) In above Fibocci series, it can be seen that every 3rd number is even. Using the same logic

a=1
b=2
sum=0
c=0
limit = 4000000

while c<limit:
    sum+=b
    c=a+b
    a=c+b
    b=c+a
   
print(sum)


#approach 3) If we only write even numbers, it can be seen that 2 8 34 have a pattern .. 34 = 4*8 + 2 and the ppatern follows  144 = 34*4 + 8

a=2 #first vale needs to be changed as we know
b=8 #value changed as we know
c=34
sum=10
limit = 4000000

while c<limit:
    sum+=c
    a=b
    b=c
    c=4*b +a

print(sum)
    




# Above C < limit works correct instead of a or b, so as to include a or b in the sum if it is less than 4M