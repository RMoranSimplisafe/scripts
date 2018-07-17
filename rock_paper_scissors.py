#!/usr/bin/env python3

from random import randint

user_input = input()
valid_moves = ['rock', 'paper', 'scissors']

def computer_move():
    return valid_moves[randint(0,2)]

while user_input not in valid_moves:
    print "Don't be dumb! Write rock, paper, or scissors."
    user_input = input()
    
print computer_move()
