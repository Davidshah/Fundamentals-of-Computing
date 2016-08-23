# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100
num = 0
remain = 7

# helper function to start and restart the game
def new_game():
    # remove this when you add your code
    global num_range
    global num
    global remain
    num = random.randint(0, num_range)
    
    print "New game. Range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(remain)
    print ""


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    global remain
    
    num_range = 100
    remain = 7
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global remain
    
    num_range = 1000
    remain = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global num
    global remain
    guess1 = int(guess)
    print "Guess was " + guess
    
    if guess1 == num and remain >= 1:
        remain = remain - 1
        print "Number of remaining guesses is " + str(remain)
        print "Correct!"
        print ""
        num_range = 100
        remain = 7
        new_game()
    elif guess1 < num and remain >= 1:
        remain = remain - 1
        print "Number of remaining guesses is " + str(remain)
        print "Higher!"
        print ""
    elif guess1 > num and remain >= 1:
        remain = remain - 1
        print "Number of remaining guesses is " + str(remain)
        print "Lower!"
        print ""
    else:
        print "You have ran out of guesses. Please try again"
        print ""
        num_range = 100
        remain = 7
        new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
