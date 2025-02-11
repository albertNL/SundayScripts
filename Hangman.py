import random
HANGMAN_ASCII = ['''
   *----*
        |
        |
        |
        |
       ===''', '''
   *----*
   |    |
        |
        |
        |
        |
       ===''', '''
   *----*
   |    |
   O    |
        |
        |
        |
       ===''', '''
   *----*
   |    |
   O    |
   |    |
        |
        |
       ===''', '''
   *----*
   |    |
   O    |
  /|    |
        |
        |
       ===''', '''
   *----*
   |    |
   O    |
  /|\   |
        |
        |
       ===''', '''
   *----*
   |    |
   O    |
  /|\   |
  /     |
        |
       ===''', '''
   *----*
   |    |
   O    |
  /|\   |
  / \   |
        |
       ===''']
wordList = 'table closet chair desk bed cupboard fridge freezer couch'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:   
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstovwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('Welcome to Hangman! Try to guess the word by choosing the right letters. Rules: only pick letters and only one letter per try. Let the games begin!')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(wordList)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! the secret word is "' + secretWord + '"! You have won!')
            gameIsDOne = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + 'missed guesses and ' +
                  str(len(correctLetters)) + 'correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
                  missedLetters = ''
                  correctLetters = ''
                  gameIsDone = False
                  secretWord = getRandomWord(words)
        else:
            break
