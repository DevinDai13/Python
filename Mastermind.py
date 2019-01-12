import random

print("Welcome to Mastermind")
print(' ')

# keep asking for input as long as the input is not valid
length_input = input('What size of patterns do you wan (4 or 5)? ')
while True:
    if length_input != '4' and length_input != '5':
        length_input = input('What size of patterns do you want (4 or 5)? ')
    else:                                   # only break when input is either 4 or 5
        break

# keep asking for input as long as the input is not valid
tries = input('How many tentatives max(10 to 12)? ')
while True:
    if tries != '10' and tries != '11' and tries != '12':
        tries = input('How many tentatives max(10 to 12)? ')
    else:                                     # only break when input is either 10, 11 or 12
        break

# initialize the valid letter list, playing is True, attempt is 0 in the beginning, history list for displaying
# every past result when a new guess is entered.
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
playing = True
attempts = 0
history_list = []

# computer is the mastermind which randomly picks four / five secret code depending on the input the player enters
message = ''
if length_input == '4':
    message = random.sample(letters, 4)
elif length_input == '5':
    message = random.sample(letters, 5)
print(message)

# display prompt and input, check all input length and whether the input letters are in the given range
while playing:
    correct_message_list = list(message)  # make the message into a list

    # when they tries run out, display the lose message and playing is set to false
    if attempts == int(tries):
        print('Your attempts are over. You lose.')
        print('Secret Code: ' + str(correct_message_list))
        playing = False
        break
    attempts += 1   # update attempts

    player_guess = input('Guess code of ' + length_input + ' with alphabet [A..H]: ')
    player_guess = player_guess.upper()   # transform all input into capitals so player can enter either caps or lower

    # if the you input 'exit' as a input guess, the game stops and quits
    if player_guess == 'EXIT':
        print(' ')
        print('Thanks for playing.')
        playing = False
        break

    # checking if player's input length is correct. If not the same then just ask the prompt again until correct input
    if len(player_guess) != len(message):
        continue

    # checking if player's input is with in the range of the valid letters
    # If not the same then just ask the prompt again until correct input
    list_guessed_message = list(player_guess)
    valid_range = True
    for i in range(int(length_input)):
        if list_guessed_message[i] not in letters:
            valid_range = False
            continue

    # when they win, display the winning message and playing is set to false
    if list_guessed_message == correct_message_list:
        print('You win!')
        print('Secret Code: ' + str(correct_message_list))
        playing = False
        break

    # '+' == correctly positioned letter   '-' == correctly guessed letter but wrongly positioned   .
    #  '.' == wrongly selected letters

    # comparison between player's input and secret code
    right_pos = 0           # these three variables are counters for each of the three symbols
    right_letter = 0
    wrong_letter = 0

    for i in range(int(length_input)):
        # if each letter in guess list and each letter in correct message is the same, then right_pos increments by 1
        if list_guessed_message[i] == correct_message_list[i]:
            right_pos += 1

        # if any letter in guess list is in correct message but not the same position
        # then right_letter increments by 1
        elif list_guessed_message[i] in set(correct_message_list) and list_guessed_message[i] != correct_message_list[i]:
            right_letter += 1

        # if any letters in guess list is not in the correct message , then wrong_letter increments by 1
        elif list_guessed_message[i] not in set(correct_message_list):
            wrong_letter += 1

    # if the length and letter range are the are correct, then display the result of your guess
    if len(player_guess) == len(message) and valid_range:
        # result if the guess in list form and the hints
        # append the result to the history list and the for loop is for printing all the previous guesses
        # as well as the most current one
        result = str(list_guessed_message) + ' (' + str('+'*right_pos) + str('-'*right_letter) + str('.'*wrong_letter) + ')'
        history_list.append(result)
        for line in history_list:
            print(line)





