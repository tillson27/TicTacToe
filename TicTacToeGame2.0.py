#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:36:50 2020

@author: joshtillson
"""


#============================================
#Game/main function 
def game():
    print("Welcome to TicTacToe!")
    print("Two players are required to play")
    print("Player 1 are Xs")
    print("Player 2 are Os \n")
    line1 = "__1__|__2__|__3__"
    line2 = "__4__|__5__|__6__"
    line3 = "  7  |  8  |  9  "
    print(line1)
    print(line2)
    print(line3)
    game_over = False
    p1_moves = []
    p2_moves = []
    
    while not game_over:
        p1_move1 = input("When ready player 1 enter the " + 
                         " number of the box you wish to fill: ")
    
    
        if int(p1_move1) < 1 or int(p1_move1) > 9:
            p1_move1 = input("Sorry your number must be between 1 and 9 \n" +
                           "Please try again: ")
        
        for el in p1_moves:
            if p1_move1 == el:
                p1_move1 = input("This space has already been filled. Please try again!")
                break
            
        for el in p2_moves:
            if p1_move1 == el:
                p1_move1 = input("This space has already been filled. Please try again!")
                break
        
            
        p1_moves.append(p1_move1)
        
        if int(p1_move1) < 4:
            line1 = player1_move(line1, line2, line3, p1_move1)
        elif int(p1_move1) < 7:
            line2 = player1_move(line1, line2, line3, p1_move1)
        else:
            line3 = player1_move(line1, line2, line3, p1_move1)
            
        
        print("")    
        print(line1)
        print(line2)
        print(line3)
        
        if winner(p1_moves):
            print("")
            print("Congradulations Player 1, you win!")
            game_over = True
            break
        
        elif cats_game(p1_moves,p2_moves):
            print("")
            print("Oh no! It's a cats game! Player 1 and Player 2 tie.")
            game_over = True
            break
            
        
        print("") 
        p2_move1 = input("Now it's your turn Player 2, enter the number " +
                         " of the spot you wish to fill: ")
        
        if int(p1_move1) < 1 or int(p1_move1) > 9:
            p2_move1 = input("Sorry your number must be between 1 and 9 \n" +
                           "Please try again: ")
            
        for el in p1_moves:
            if p2_move1 == el:
                p2_move1 = input("This space has already been filled. Please try again!")
                break
            
        for el in p2_moves:
            if p2_move1 == el:
                p2_move1 = input("This space has already been filled. Please try again!")
                break
            
        p2_moves.append(p2_move1)
        
        if int(p2_move1) < 4:
            line1 = player2_move(line1, line2, line3, p2_move1)
        elif int(p2_move1) < 7:
            line2 = player2_move(line1, line2, line3, p2_move1)
        else:
            line3 = player2_move(line1, line2, line3, p2_move1)
        
        print("")    
        print(line1)
        print(line2)
        print(line3)
        
        if winner(p2_moves):
            print("")
            print("Congradulations Player 2, you win!")
            game_over = True
            break
        
        elif cats_game(p1_moves,p2_moves):
            print("")
            print("Oh no! It's a cats game! Player 1 and Player 2 tie.")
            game_over = True
            break
        
    print("")
    replay = input("Would you like to play again Yes or No: ")
    while not replay == "Yes" and not replay == "No":
        replay = input("Not a valid answer, please input Yes or No: ")
    if replay == "Yes":
        print("")
        print("")
        game()
    print("")    
    print("Thanks for playing!")

    
#============================================
#Function for player one move    

def player1_move(line1, line2, line3, move):
    if int(move) < 4:
        n = 0
        for char in line1:
            n += 1
            if char == move:
                line1 =  line1[0:n-1] + "X_" + line1[n+1::]
        return line1
    elif int(move) < 7:
        n = 0
        for char in line2:
            n += 1
            if char == move:
                line2 =  line2[0:n-1] + "X_" + line2[n+1::]
        return line2
    else:
        n = 0
        for char in line3:
            n += 1
            if char == move:
                line3 =  line3[0:n-1] + "X " + line3[n+1::]
        return line3
    
#============================================             
#Function for player two move

def player2_move(line1, line2, line3, move):
    if int(move) < 4:
        n = 0
        for char in line1:
            n += 1
            if char == move:
                line1 =  line1[0:n-1] + "O_" + line1[n+1::]
        return line1
    elif int(move) < 7:
        n = 0
        for char in line2:
            n += 1
            if char == move:
                line2 =  line2[0:n-1] + "O_" + line2[n+1::]
        return line2
    else:
        n = 0
        for char in line3:
            n += 1
            if char == move:
                line3 =  line3[0:n-1] + "O " + line3[n+1::]
        return line3
    
#============================================             
#Function to check for a winner
# 8 ways to win 
# 1,2,3 or 1,4,7 or 2,5,8 or 3,6,9 or 4,5,6 or 7,8,9 or 1,5,9 or 7,5,3
        
def winner(m):
    winners = [[1,2,3],[1,4,7],[2,5,8],[3,6,9],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]
    new_list = []
    for s in m:
        new_list.append(int(s))
    new_list.sort()
    if new_list in winners:
        return True
    else:
        return False
    
#============================================             
#Catsgame --> the board is full
        
def cats_game(p1_moves, p2_moves):
    return (len(p1_moves) + len(p2_moves)) == 9
        

        

game()