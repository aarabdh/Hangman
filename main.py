from Hangman import Hangman as h
from random import randint
words = ['hilarious', 'pocket', 'wealthy', 'guitar', 'page', 'night', 'tasteful', 'suppose', 'guarded', 'plug', 'women', 'bulb', 'pentagon']
k = words[randint(0, len(words)-1)]
a = h(word = k)
a.initial()
b = input("Enter your guess here: ")
while True:
    a.nextOut(b)
    b = input("Enter your guess here: ")
