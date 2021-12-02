import random
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)
lives = 6

print(logo)

display = []
lose = False

for i in range(len(chosen_word)):
    display.append('_')

while '_' in display and not lose:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in display:
        print(f'You have already guessed letter {guess_letter}')

    for i in range(len(chosen_word)):
        if guess_letter == chosen_word[i]:
            display[i] = guess_letter
    if guess_letter not in chosen_word:
        print(f'{guess_letter} is not in the word. You lose a life.')
        lives-=1
        if lives<=0:
            lose = True

    print(display)
    print(stages[lives])

if(lose):
    print('You lose!')
    print(f'The answer is {chosen_word}')
else:
    print('You Win!')