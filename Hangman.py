user_name = input('\nEnter Your Name:    ').upper()
print(f'\n\nGREETINGS {user_name}, WELCOME TO HANGMAN')
                                                                              
dict_of_words = {'Shivaji':'_______', 'Pratap':'______', 'Kumbha':'______', 'Bajirao':'_______', 'Shambhaji':'_________'}
# Note - 1 
# Simply adding more items to dictionary will automatically 
# # increase the game level and no of words to guess 
condition = True                                                              
Level = 0
for i in range(len(dict_of_words)):
    no_of_guesses = 3
    Level += 1
    Word_to_guess = list(list(dict_of_words.keys())[i].lower())

    equator = Word_to_guess.copy()

    word_guessed = list(list(dict_of_words.values())[i].lower())

    while condition == True:
        if no_of_guesses == 0:
            condition = False
        
        else:
            if word_guessed == equator:

                print(f'\n\nCongratulations {user_name}! You have cleared Level {Level}')

                print(f'\nYou have correctley Guessed the word {list(dict_of_words.keys())[i]}')
                print(f'And you still had {no_of_guesses} guesses left.\n')
                


                if Level == len(dict_of_words):
                    print(f'CONGRATULATIONS {user_name} ! YOU ARE THE HANGMAN CHAMPION\n')
                    print(f'YOU HAVE CLEARED ALL THE {Level} LEVELS SUCCEFULLY\n')
                    condition = False
                else:
                    print('DO YOU WANT TO GO TO THE NEXT LEVEL\n')

                    print('If YES then press Enter')
                    print('If NO then press any key and then hit Enter\n')
                    y_n = input('Enter your response:    ')

                    if y_n == '':

                        break

                    else:
                        print(f'\n{user_name} is a Level {Level} Winner\n\n      GAME OVER  ')
                        condition = False
            else:
                print(f'\n\nLevel {Level}\n')
                user_guess = input('Enter your Guess:   ')
                if user_guess in Word_to_guess:

                    indox = Word_to_guess.index(user_guess)

                    word_guessed[indox] = user_guess

                    Word_to_guess[indox] = '_'

                    print('\n  Your Guess is correct guess another  \n')

                    print(f'\nYour guessed word is {word_guessed}')

                elif user_guess not in Word_to_guess:

                    no_of_guesses -= 1
                    print(f'\nYour guessed word is {word_guessed}')
                    print(f'\nYour Guess is incorrect, Try Again')

                    print(f'You only have {no_of_guesses} Guesses left')

                else:

                    no_of_guesses -= 1

                    print('\nInvalid Guess, Try Again')
                    print(f'\nYour guessed word is {word_guessed}')
                    print(f'You only have {no_of_guesses} Guesses left')