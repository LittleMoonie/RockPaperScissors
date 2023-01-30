import random
import os

def clrscr():
  """ Clears the console in order to make a more pleasant game """
  if os.name == "posix":  # compatible with Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):  # compatible with DOS/Windows
    os.system('CLS')

def playerFavored(answer):
    options = ['rock', 'paper', 'scissors']
    probabilities = [[0.3, 0.2, 0.5],[0.5, 0.3, 0.2],[0.2, 0.5, 0.3]]
    if answer not in options:
        return print('Invalid input')
    else:
        choices = random.choices(options, weights=probabilities[options.index(answer)], k=1)
        if answer == choices[0]:
            clrscr()
            return print(f"It's a tie! You picked {answer} and the bot picked {choices[0]}!")

        elif answer == 'rock' and choices[0] == 'scissors' or answer == 'scissors' and choices[0] == 'paper' or answer == 'paper' and choices[0] == 'rock':
            clrscr()
            return print(f'\nYou won! You picked {answer} and the bot picked {choices[0]}!')

        else:
            clrscr()
            return print(f'\nYou lost! You picked {answer} and the bot picked {choices[0]}!')

def normal(answer):
    options = ['rock', 'paper', 'scissors']
    choice = random.choice(options)

    if answer not in options:
        return print('Invalid input')

    else:
        if answer == 'rock':
            if choice == 'rock':
                clrscr()
                return print(f"It's a tie! You picked {answer} and the bot picked {choice}!")

            elif choice == 'paper':
                clrscr()
                return print(f'\nYou lost! You picked {answer} and the bot picked {choice}!')

            elif choice == 'scissors':
                clrscr()
                return print(f'\nYou won! You picked {answer} and the bot picked {choice}!')

        elif answer == 'paper':
            if choice == 'rock':
                clrscr()
                return print(f'\nYou won! You picked {answer} and the bot picked {choice}!')

            elif choice == 'paper':
                clrscr()
                return print(f"It's a tie! You picked  {answer} and the bot picked {choice}!")

            elif choice == 'scissors':
                clrscr()
                return print(f'\nYou lost! You picked {answer} and the bot picked {choice}!')

        elif answer == 'scissors':
            if choice == 'rock':
                clrscr()
                return print(f'\nYou lost! You picked {answer} and the bot picked {choice}!')

            elif choice == 'paper':
                clrscr()
                return print(f'\nYou won! You picked {answer} and the bot picked {choice}!')
                
            elif choice == 'scissors':
                clrscr()
                return print(f"It's a tie! You picked {answer} and the bot picked {choice} !")


def botFavored(answer):
    options = ['rock', 'paper', 'scissors']
    probabilities = [[0.3, 0.5, 0.2],[0.2, 0.3, 0.5],[0.5, 0.2, 0.3]]
    if answer not in options:
        return print('Invalid input')

    else:
        choices = random.choices(options, weights=probabilities[options.index(answer)], k=1)
        if answer == choices[0]:
            clrscr()
            return print(f"It's a tie! You picked {answer} and the bot picked, choices[0]!")

        elif answer == 'rock' and choices[0] == 'scissors' or answer == 'scissors' and choices[0] == 'paper' or answer == 'paper' and choices[0] == 'rock':
            clrscr()
            return print(f'\nYou won! You picked {answer} and the bot picked {choices[0]}!')

        else:
            clrscr()
            return print(f'\nYou lost! You picked {answer} and the bot picked {choices[0]}!')


def impossible(answer):
    options = ['rock', 'paper', 'scissors']

    if answer not in options:
        return print('Invalid input')

    else:
        if answer == 'rock':
            clrscr()
            return print(f'\nYou lost! You picked {answer} and the bot picked paper!')

        elif answer == 'paper':
            clrscr()
            return print(f'\nYou lost! You picked {answer} and the bot picked scissors!')

        elif answer == 'scissors':
            clrscr()
            return print(f'\nYou lost! You picked {answer} and the bot picked rock!')

counter = 0
print(f'\n\nWelcome to a game of rock paper scissors! This game of rock paper scissors has 4 different levels being "Player Favored", "Normal", "Bot Favored", "Impossible".\n')

while True :
    counter = counter + 1
    if counter < 2:
        readyCheck = input(f'\nAre you ready to start a game of Rock Paper Scissors? Y/N.\n').casefold()
    else:
        readyCheck = input(f'\nAre you ready to start a game of Rock Paper Scissors? Y/N. You can change game levels by continuing with pressing "Y".\n').casefold()

    if readyCheck == 'y' or readyCheck == 'yes' or readyCheck == 'ye':
        while True:
            level = input('\nWhat level do you wish to play against? Please enter either "Player Favored", "Normal", "Bot Favored", or "Impossible".\n').casefold()
            if level == 'player favored' or level == 'normal' or level == 'bot favored' or level == 'impossible':
                while True : 
                    answer = input('\nWhat do you wish to pick? Rock, Paper, Scissors.\n').casefold()
                    
                    if answer == 'rock' or answer == 'paper' or answer == 'scissors':
                        match level:

                            case 'player favored':
                                playerFavored(answer)
                                break;

                            case 'normal':
                                normal(answer)
                                break;


                            case 'bot favored':
                                botFavored(answer)
                                break;


                            case 'impossible':
                                impossible(answer)
                                break;

                        break;
                    else :
                        print(f'\nYou entered "{answer}" which is not part of the provided playable choices. Please enter either Rock, Paper or Scissors.\n')
                break;
            else : 
                print(f'\nYou entered "{level}" which is not part of the provided level choices. Please enter either "Player Favored", "Normal", "Bot Favored", or "Impossible".\n')

    elif readyCheck.casefold() == 'n' or readyCheck.casefold() == 'no':
        print('Feel free to start a game of Rock, Paper, Scissors whenever you feel like it.\nGood day to you!')
        break;
    else :
        print(f'\nYou entered "{readyCheck}" which is not part of the provided choices. Please enter either "Y" or "N" to proceed.')
