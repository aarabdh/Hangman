import time

class Hangman():
    def __init__(self, word) -> None:
        self.guesses = []
        self.wrong = 0
        self.arr = ['_']*len(word)
        self.word = word.lower()
        self.hangman = ['   _____ \n  |     |\n  |     \n  |    \n  |    \n  |      \n  |      \n__|__\n'
    , '   _____ \n  |     |\n  |     O\n  |    \n  |    \n  |      \n  |      \n__|__\n'
    , '   _____ \n  |     |\n  |     O\n  |     |\n  |    \n  |      \n  |      \n__|__\n'
    , '   _____ \n  |     |\n  |     O\n  |    /|\n  |    \n  |      \n  |      \n__|__\n'
    , '   _____ \n  |     |\n  |     O\n  |    /|\\\n  |    \n  |      \n  |      \n__|__\n'
    , '   _____ \n  |     |\n  |     O\n  |    /|\\\n  |    / \n  |      \n  |      \n__|__\n'
    , '   _____ \n  |     |\n  |     O\n  |    /|\\\n  |    / \\\n  |      \n  |      \n__|__\n']

    def guess(self, letter) -> int:
        letter = letter.lower()
        flag = False
        if letter in self.guesses:
            return -1
        self.guesses.append(letter)
        for idx, i in enumerate(self.word):
            if i == letter:
                self.arr[idx] = letter
                flag = True
        if flag:
            return 1
        return 0

    def initial(self):
        print("Hey! Welcome to my version of the game Hangman!\nAll you have to do is enter a letter and press enter.")
        print(' '.join(self.arr))
        print(self.hangman[0])
        pass

    def nextOut(self, letter):
        if len(letter) > 1:
            print("Please enter a single letter!")
            return
        elif letter == " ":
            print("Space is not recognized as a character in this game.\nPlease enter an albhabetic character.")
            return
        elif str(letter).isdigit():
            print("Please enter an albhabet, this word does not contain digits.")
            return
        elif not str(letter).isalpha():
            print("Please enter only alphabetic characters.")
            return
        yo = self.guess(letter = letter)
        if yo == 0:
            self.wrong+=1
            if self.wrong==6:
                print("You have exhausted your chances!")
                print(self.hangman[self.wrong])
                print(f"The word was {self.word}")
                print("Better luck next time!")
                time.sleep(5)
                quit()
            print(f"Incorrect! You have {6-self.wrong} chances left.")
            print(f"Guesses so far: {','.join(self.guesses)}")
            print(' '.join(self.arr))
            print(self.hangman[self.wrong])
        elif yo == 1:
            if ''.join(self.arr) == self.word:
                print("Congrats, you won!")
                print(f"You correctly guessed that the word was '{self.word}'!")
                print("The man was saved from hanging")
                print("If you liked the game, do give it another shot!")
                time.sleep(5)
                quit()
            print(f"Correct! The letter {letter} is found within the word!")
            print(f"Guesses so far: {','.join(self.guesses)}")
            print(' '.join(self.arr))
            print(self.hangman[self.wrong])
        elif yo == -1:
            print(f"You have guessed {letter} already! Please try a different guess.")
            print(f"Guesses so far: {','.join(self.guesses)}")
            print(' '.join(self.arr))
            print(self.hangman[self.wrong])