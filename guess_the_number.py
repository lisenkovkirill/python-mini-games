from random import randint

def computer_number(min_num,max_num):
    return randint(min_num,max_num)

def player_guess(min_num,max_num):
    user_input = int(input(f'Guess a number between {min_num} and {max_num}: '))
    return user_input

def checking(num, min_num, max_num):
    if min_num<=num<=max_num:
        return True
    else:
        return False


def play():
    low = int(input('Write the lower border of guessing: '))
    high = int(input('Write the higher border of guessing: '))
    number_of_tries = 1
    computer_choice = computer_number(low,high)
    player_choice = player_guess(low,high)
    while player_choice != computer_choice:
        if player_choice>computer_choice:
            player_choice = int(input('Number is too high, try again: '))
            number_of_tries += 1
        elif player_choice<computer_choice:
            player_choice = int(input('Number is too low, try again: '))
            number_of_tries += 1

    print (f'Congratulation! You managed to guess the number {computer_choice}.')
    if number_of_tries == 1:
        print(f'It took you {number_of_tries} try.')
    else:
        print (f'It took you {number_of_tries} tries.')

play()