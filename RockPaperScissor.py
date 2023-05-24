import random


List1 = ['Rock','Paper','Scissor']
    


def win_logic(Player_Choice,Computer_choice):

    if Player_Choice==Computer_choice:
        return 0
    elif Player_Choice=='Rock' and Computer_choice =='Scissor':
        return 1#'Player has won by selecting Rock'
    elif Player_Choice=='Scissor' and Computer_choice == 'Paper':
        return  1#'Player has won by selecting Scissor'
    
    elif Player_Choice == 'Paper' and Computer_choice =='Rock':
        return 1#'Player has won by selecting Paper'
    
    else:
        return -1#f'Computer has won by selecting {Computer_choice}',
    

Matches_played = 0
Player_won = 0
computer_won =0
Matches_drawn=0


while True:
    Matches_played = Matches_played +1
    
    Player_Choice = int(input('Enter any of the value /n 0:Rock 1:Paper 2:Scissor'))
    if Player_Choice >=0 and Player_Choice<=2:
        Player_Choice = List1[Player_Choice]
    else:
        print('Enter correct value')
        continue  # to repeat the loop

    Computer_choice = random.choice(List1)
    print('Player has choosen ',Player_Choice)
    print('Computer has choosen',Computer_choice)
    a = win_logic(Player_Choice,Computer_choice)

    if a==1:
        print(f'Player has won by selecting {Player_Choice}')
        Player_won = Player_won +1
    elif a==0:
        print(f'Computer has won by selecting {Player_Choice}')
        computer_won = computer_won+1
    else:
        print('Match Drawn')
        Matches_drawn = Matches_played - (Player_won+computer_won)
        


    play_again = input('Enter any key to play again  Or q to quit')
    if play_again =='q' or play_again =='Q':
        break


print('Thanks for playing')

print('Matches_played',Matches_played)
print('Player_won',Player_won)
print('computer_won',computer_won)
print('Matches_drawn',Matches_drawn)
