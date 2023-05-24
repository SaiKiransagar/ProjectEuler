def printGame():
    zero = 'X' if xState[0] else ('0' if OState[0] else 0)
    one = 'X' if xState[1] else ('0' if OState[1] else 1)
    two= 'X' if xState[2] else ('0' if OState[2] else 2)
    three = 'X' if xState[3] else ('0' if OState[3] else 3)
    four= 'X' if xState[4] else ('0' if OState[4] else 4)
    five = 'X' if xState[5] else ('0' if OState[5] else 5)
    six= 'X' if xState[6] else ('0' if OState[6] else 6)
    seven = 'X' if xState[7] else ('0' if OState[7] else 7)
    eight = 'X' if xState[8] else ('0' if OState[8] else 8)

    print(f"{zero}|{one}|{two}")
    print(f"{three}|{four}|{five}")
    print(f"{six}|{seven}|{eight}")


def winFactor():

    winChances = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


    for win in winChances:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            print('X Wins!!')
            printGame()
            return 1

        elif OState[win[0]] + OState[win[1]] + OState[win[2]] == 3:
            print('0 Wins!!')
            printGame()
            return 1

    total = sum(xState) + sum(OState)

    if total == 9:
        print('Match Drawn')
        return 1
        

    return -1
            
            




if __name__ == "__main__":

    xState = [0,0,0,0,0,0,0,0,0]
    OState = [0,0,0,0,0,0,0,0,0]

    


    print("Welcome to Tic Tac Toe")

    turn = 'X'

    while True:
        printGame()
        

        

        if turn =='X':
            print('X Choice')
            position = int(input("Position you would like to enter X:"))
            
            try:
                if xState[position] == 1 or OState[position] == 1:
                    raise ValueError('You have enteretd number which is already played. Please enter correct number now')
                                                                        
            except ValueError as e:
                print(e)
                turn ='X'
                
            except Exception:
                print('You have enteretd incorrect number. The number is out of the options {0-8}. Please enter correct number now')
                turn ='X'

            else:
                xState[position] = 1
                turn = '0'
                
                

        else:
            print('0 Choice')
            position = int(input("Position you would like to enter 0:" )) 

            try:
                if OState[position] == 1 or xState[position] == 1:
                    raise ValueError('You have enteretd number which is already played. Please enter correct number now')
                                                                        
            except ValueError as e:
                print(e)
                turn ='0'
                
            except IndexError:
                print('You have enteretd incorrect number. The number is out of the options {0-8}. Please enter correct number now')
                turn ='0'

            else:
                OState[position] = 1
                turn = 'X'

        c = winFactor()

         if c!=-1:
            print("Match over")
            break


        


        
    

