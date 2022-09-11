import random


def play_game():
    run = True

    computer_words = ['rabbit', 'donkey', 'horse', 'aardvark', 'snake', 'eel', 'elephant', 'armadillo', 'platypus']

    blank_list = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', ]

    secret_word = random.choice(computer_words)
    secret_characters = [*secret_word]

    print(blank_list[0:len(secret_characters)])

    wrong_guesses = 0

    while run:
        player_guess = input("Guess a Letter or the Word: ").lower()

        if player_guess == secret_word:
            print(secret_word + '!')
            print('Correct! You Win!')
            break

        elif player_guess in secret_characters:

            for i in range(len(secret_characters)):
                if secret_characters[i] in player_guess:
                    blank_list[i] = player_guess

                    print(blank_list[0:len(secret_characters)])

            continue

        if secret_characters == blank_list[0:len(secret_characters)]:
            print(secret_word + '!')
            print('Correct! You Win!')

            break

        elif player_guess not in secret_characters:
            print('Wrong!')
            wrong_guesses += 1

        if wrong_guesses == 1:
            print('0')
        if wrong_guesses == 2:
            print('0\n'
                  '|')
        if wrong_guesses == 3:
            print(' 0\n'
                  '/|')
        if wrong_guesses == 4:
            print(' 0\n'
                  '/|\\')
        if wrong_guesses == 5:
            print(' 0\n'
                  '/|\\\n'
                  ' /')
        if wrong_guesses == 6:
            print(' 0\n'
                  '/|\\\n'
                  ' /\\')
            print('You Lose!')
            break

    play_again = input('Play Again?(y/n): ').lower()

    if play_again == 'y':
        play_game()

    elif play_again == 'n':
        quit()


play_game()
