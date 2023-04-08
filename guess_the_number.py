from random import randint


def computer_number(min_num,max_num):
    '''
    function that generates a random number based on the range passed as args.
    returns random int
    '''
    return randint(min_num,max_num)


def players_first_guess(min_num,max_num):
    '''
    function that asks the player for the first correct number.
    returns random int
    '''
    while True:
        user_input = int(input(f'Guess a number between {min_num} and {max_num}: '))
        if checking(user_input, min_num, max_num):
            return user_input
        else:
            print(f'Incorrect. Try again.')


def checking(num, min_num, max_num):
    '''
    function that checks that the player's number is correct.
    returns bool
    '''
    if min_num<=num<=max_num:
        return True
    else:
        return False


def main_game():
    print("Hello! It's the game 'Guess the number'. Follow the instructions!")
    low = int(input('Write the lower border of guessing: '))
    high = int(input('Write the higher border of guessing: '))
    print('If you want to quit the game, you can write "stop" after the 1st try')
    number_of_tries = 1
    computer_choice = computer_number(low, high)
    player_choice = players_first_guess(low, high)
    while player_choice != computer_choice:
        if player_choice > computer_choice:
            while True:
                player_choice = input('Number is too high, try again: ')
                if player_choice == "stop":
                    print('You decided to stop the game.')
                    return None
                elif checking(int(player_choice), low, high):
                    player_choice = int(player_choice)
                    number_of_tries += 1
                    break
                else:
                    print(f'Incorrect. Try again.')
        elif player_choice < computer_choice:
            while True:
                player_choice = input('Number is too low, try again: ')
                if player_choice == "stop" or player_choice == "Stop":
                    print('You decided to stop the game.')
                    return None
                elif checking(int(player_choice), low, high):
                    player_choice = int(player_choice)
                    number_of_tries += 1
                    break
                else:
                    print(f'Incorrect. Try again.')

    print (f'Congratulation! You managed to guess the number {computer_choice}.')
    if number_of_tries == 1:
        print(f'It took you {number_of_tries} try.')
    else:
        print(f'It took you {number_of_tries} tries.')


main_game()