import random

def display_word(matrix):
    display = ''
    print()
    for i in range(len(matrix)):
        display += matrix[i]
    print(display)

def reveal_letter(input_letter, answer_matrix, correct_answer):
    for i in range(len(correct_answer)):
        if input_letter == correct_answer[i]:
            answer_matrix[i] = input_letter
    return answer_matrix



lives = 8
dictionary = ['python', 'java', 'kotlin', 'javascript']
ASCII_lowercase = 'qwertyuiopasdfghjklzxcvbnm'
correct_answer = random.choice(dictionary)

answer_matrix = []
guessed_letters = ''
for i in range(len(correct_answer)):
    answer_matrix.append('-')

print("H A N G M A N")
choice = ''

while choice != 'play' and choice != 'exit':
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == 'play':
        while lives > 0:
            display_word(answer_matrix)
            input_letter = input("Input a letter: ")

            if len(input_letter) != 1:
                print("You should print a single letter.")
                continue

            if input_letter not in ASCII_lowercase:
                print("It is not an ASCII lowercase letter.")
                continue

            if input_letter in guessed_letters:
                print("You already typed this letter.")
                continue

            if input_letter in correct_answer:
                if input_letter not in guessed_letters:
                    answer_matrix = reveal_letter(input_letter, answer_matrix, correct_answer)
                    guessed_letters += input_letter

            if input_letter not in correct_answer:
                guessed_letters += input_letter
                print("No such letter in the word!")
                lives -= 1

            if '-' not in answer_matrix:
                break

        if lives == 0:
            print("You are hanged!")
        else:
            print("You guessed the word!")
            print("You survived!")



