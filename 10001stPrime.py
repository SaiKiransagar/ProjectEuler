import itertools

b=[]

for i in itertools.count(2):
    if len(b)==100:
        break
    for j in range(2,i):
        if i%j==0:
            break
    else:
        b.append(i)
print(max(b))

#https://www.xarg.org/puzzle/project-euler/problem-7/
#for better solution
