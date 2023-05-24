x1 = int(input('Enter first number : '))
x2 = int(input('Enter second number : '))

for i in range (x1,x2):
    
    x=i
    List_of_numbers = []

    while x!=1:
        if x%2==0:
            x=int(x/2) #to remove decimal
        else:
            x=x*3+1
            
        if x in List_of_numbers:
            x=0
            List_of_numbers = []  #this can be used to check if any number do not obey theorem
            break
        else:
            List_of_numbers.append(x)
            pass
            
            
        
        if x == 0:
            break
        else:
            pass
    print(List_of_numbers)
    print(i,len(List_of_numbers))
    

