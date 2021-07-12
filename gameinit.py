#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:57:59 2021

@author: marcinswierczewski
"""

import pygame
import sys
import time 
import Tictactoe as T
import random

# setting default metrics 
user = None
pygame.init()
# Below is for switching between PvAI and AIvAI
AIsimulation = False
aiturn = False
# after first move this would become False for AIvAI mode
firstmove = True

WIDTH = 600
HEIGHT = 600
MAINCOLOR = (255, 255, 255)
BACKCOLOR = (0,0,0)
font = "BitPap.ttf"
evilfont = "WitchingHour.ttf"
evilfont2= "hothead_.ttf"
# sillyfont2 = "StickLetterMedium.ttf"
sillyfont2 = "This Is Ridiculous.ttf"
grave = "DIEDIEDI.TTF"
largefont = pygame.font.Font(font, 30)
smallfont = pygame.font.Font(font, 20)
verylargefont = pygame.font.Font(font, 40)

screen = pygame.display.set_mode( (WIDTH, HEIGHT))
pygame.display.set_caption("Marcin's game of TictacToe")
screen.fill(MAINCOLOR)

# getting board from tictactoe module
board = T.initial_state()

# loop for main game
while True:
    # standard exit code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.update()
    
    # initiating the menu screen, if user is not picked
    if user == None:
        title = verylargefont.render("Marcin's game of TictacToe", True, BACKCOLOR)
        # this is creating surface of a size of text and coordinates (0,0)
        titlerec =  title.get_rect()
        # changing deafult coordinates 
        titlerec.center = ((WIDTH/2),120)
        # blit draws title onto rectangle
        screen.blit(title,titlerec)
        
        # drawing rectangles for buttons, on the screen 
        xbutton = pygame.Rect(50, 200, 200, 50)
        pygame.draw.rect(screen, BACKCOLOR, xbutton)
        ybutton = pygame.Rect(340, 200, 200, 50)
        pygame.draw.rect(screen, BACKCOLOR, ybutton)
        
        # similar as above, printing text on the buttons
        xtext = smallfont.render("Play as X", True, MAINCOLOR)
        ytext = smallfont.render("Play as O", True, MAINCOLOR)
        xrec =  xtext.get_rect()
        yrec =  ytext.get_rect()
        xrec.center = xbutton.center
        yrec.center = ybutton.center
        screen.blit(xtext,xrec)
        screen.blit(ytext,yrec)

        # Changing graphics of the board 
        settingstitle = largefont.render("Change Board Style:", True, BACKCOLOR)
        settingsrec =  settingstitle.get_rect()
        settingsrec.center = ((WIDTH/2),(HEIGHT - 250))
        screen.blit(settingstitle,settingsrec)
        # drawing rectangles for setting buttons
        option1 = pygame.Rect(50, 380, 100, 40)
        pygame.draw.rect(screen, BACKCOLOR, option1)
        option2 = pygame.Rect(180, 380, 100, 40)
        pygame.draw.rect(screen, BACKCOLOR, option2)
        option3 = pygame.Rect(310, 380, 100, 40)
        pygame.draw.rect(screen, BACKCOLOR, option3)
        option4 = pygame.Rect(440, 380, 100, 40)
        pygame.draw.rect(screen, BACKCOLOR, option4)
        # standard printing buttom text 
        option1text = smallfont.render("Nocturnal", True, MAINCOLOR)
        option2text = smallfont.render("Evil", True, MAINCOLOR)
        option3text = smallfont.render("Crazy", True, MAINCOLOR)
        option4text = smallfont.render("Default", True, MAINCOLOR)
        
        option1rec =  option1text.get_rect()
        option2rec =  option2text.get_rect()
        option3rec =  option3text.get_rect()
        option4rec =  option4text.get_rect()

        option1rec.center = option1.center
        option2rec.center = option2.center
        option3rec.center = option3.center
        option4rec.center = option4.center
        screen.blit(option1text,option1rec)
        screen.blit(option2text,option2rec)
        screen.blit(option3text,option3rec)
        screen.blit(option4text,option4rec)
        
        
        # Options: Player vs simulation
        settings2title = largefont.render("Choose if you want to play or only simulate AI:", True, BACKCOLOR)
        settings2rec =  settings2title.get_rect()
        settings2rec.center = ((WIDTH/2),(HEIGHT - 150))
        screen.blit(settings2title,settings2rec)
        
        # setting the button for the above
        AIbutton = pygame.Rect(100, 500, 400, 50)
        pygame.draw.rect(screen, BACKCOLOR, AIbutton)
        if AIsimulation == False:
            AItext = smallfont.render("Change to AI simulation", True, MAINCOLOR)
        elif AIsimulation == True:
            AItext = smallfont.render("Change to Player vs AI", True, MAINCOLOR)
        AIrec =  AItext.get_rect()
        AIrec.center = AIbutton.center
        screen.blit(AItext,AIrec)
        
        
        # standard code for detecting click
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            # checking which area of the board is the mouse click colliding with
            if titlerec.collidepoint(mouse):
                time.sleep(0.2)
                
                title = largefont.render("paste some easter egg here", True, BACKCOLOR)
                titlerec =  title.get_rect()
                titlerec.center = ((WIDTH/2),100)
                screen.blit(title,titlerec)
            # setting player X or Y
            elif xbutton.collidepoint(mouse):
                time.sleep(0.2)
                user = T.X
            elif ybutton.collidepoint(mouse):
                user = T.O              
            # graphics options 1-4 change font style and colors 
            elif option1.collidepoint(mouse):
                time.sleep(0.1)
                BACKCOLOR = (255, 255, 255)
                MAINCOLOR = (0,0,0)
                # font = "copperplatettc"
                screen.fill(MAINCOLOR)  
                verylargefont = pygame.font.Font(grave, 40)
                largefont = pygame.font.Font(grave, 23)
                smallfont = pygame.font.Font(grave, 20)
            elif option2.collidepoint(mouse):
                time.sleep(0.1)
                BACKCOLOR = (134, 1, 17)
                MAINCOLOR = (0,0,0)
                screen.fill(MAINCOLOR)
                verylargefont = pygame.font.Font(evilfont, 40)
                largefont = pygame.font.Font(evilfont, 23)
                smallfont = pygame.font.Font(evilfont2, 20)
            elif option3.collidepoint(mouse):
                time.sleep(0.1)
                BACKCOLOR = (253, 173, 150)
                MAINCOLOR = (255, 228, 216)
                screen.fill(MAINCOLOR)
                verylargefont = pygame.font.Font(sillyfont2, 40)
                largefont = pygame.font.Font(sillyfont2, 23)
                smallfont = pygame.font.Font(sillyfont2, 20)
            elif option4.collidepoint(mouse):
                time.sleep(0.1)
                MAINCOLOR = (255, 255, 255)
                BACKCOLOR = (0,0,0)
                font = "BitPap.ttf"
                screen.fill(MAINCOLOR) 
                verylargefont = pygame.font.Font(font, 45)
                largefont = pygame.font.Font(font, 30)
                smallfont = pygame.font.Font(font, 20)
            # AI option button changes between PvAI and AIvAI modes
            elif AIbutton.collidepoint(mouse):
                # there were some lags with multiple clicks, 
                # hopefully delays can eliminate those 
                time.sleep(0.2)
                if AIsimulation == True:
                    time.sleep(0.2)
                    AIsimulation = False
                else:
                    time.sleep(0.2)
                    AIsimulation = True
    # if plalyer is created, move from menu screen to the game screen
    else:
        time.sleep(0.01)
        screen.fill(MAINCOLOR)
        tilesize = 70
        tilestart1 = (WIDTH / 2) - (1.5 * tilesize)
        tilestart2 = (HEIGHT / 2) - (1.5 * tilesize)
        tiles = []
        # creating the game board
        for i in range(3):
            row = []
            for j in range(3):
                tilerect = pygame.Rect(
                    tilestart1 + (j*tilesize),
                    tilestart2 + (i * tilesize),
                    tilesize,
                    tilesize)
                pygame.draw.rect(screen, BACKCOLOR, tilerect, 3)
                
                # rendering X or O
                if board[i][j] != T.EMPTY:
                    move = largefont.render(board[i][j], True, BACKCOLOR)
                    # rendering same as above
                    moverect = move.get_rect()
                    moverect.center= tilerect.center
                    screen.blit(move, moverect)
                row.append(tilerect)
            tiles.append(row)
        
        # setting game ending and player state 
        gameover = T.terminal(board)
        player = T.player(board)
        # checking if there's a winner
        if T.winner(board) != None:
            gameover = True
        
        # the below is for PvAI
        if AIsimulation == False:
            # Creating title above the board
            if gameover:
                if T.winner(board) == None:
                    t= "No one has won :("
                else:
                    t1  = (T.winner)
                    t = "Game Ended, GG EZ." 
            elif user != player:
                t = "AI calculating hmmmmmmmm"
            else:
                t = "Please move"
    
            gametitle = largefont.render(t, True, BACKCOLOR)
            gametitlerec =  gametitle.get_rect()
            gametitlerec.center = ((WIDTH/2),150)
            # blit draws title onto rectangle
            screen.blit(gametitle,gametitlerec)
            
            # AI move
            if (user != player 
                and gameover == False):
                if aiturn:
                    time.sleep(0.6)
                    move = T.minimax(board)
                    board = T.result(board, move)
                    aiturn = False
                else:
                    aiturn = True
    
            # checking if there's a winner after last move
            if T.winner(board) != None:
                gameover = True
                
            # User move
            click, _, _ = pygame.mouse.get_pressed()
            if (click == 1
                and user == player
                and AIsimulation == False
                and not gameover):
                mouse = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == T.EMPTY and tiles[i][j].collidepoint(mouse):
                            board = T.result(board, (i, j))
                            
        #the below is for AIvAI 
        else:
            if not gameover:
                # for better simulation, first move is random
                # in the future can train it on reinforcment learning perhaps
                if firstmove:
                    t = "AI calculating hmmmmmmmm"
                    gametitle = largefont.render(t, True, BACKCOLOR)
                    gametitlerec =  gametitle.get_rect()
                    gametitlerec.center = ((WIDTH/2),150)
                    screen.blit(gametitle,gametitlerec)
                    time.sleep(0.6)
                    
                    move = (random.randrange(0,2) , random.randrange(0,2))
                    board = T.result(board, move)
                    firstmove = False
                # further moves, after the first one
                else:
                    t = "AI calculating hmmmmmmmm"
                    gametitle = largefont.render(t, True, BACKCOLOR)
                    gametitlerec =  gametitle.get_rect()
                    gametitlerec.center = ((WIDTH/2),150)
                    # blit draws title onto rectangle
                    screen.blit(gametitle,gametitlerec)
                    time.sleep(0.6)
                    move = T.minimax(board)
                    board = T.result(board, move)
                    if T.winner(board) != None:
                        gameover = True
            # for game over:
            else:
                if T.winner(board) == None:
                    t = "No one won :(" 
                else:
                    t = "Game Ended, GG EZ." 
                gametitle = largefont.render(t, True, BACKCOLOR)
                gametitlerec =  gametitle.get_rect()
                gametitlerec.center = ((WIDTH/2),150)
                # blit draws title onto rectangle
                screen.blit(gametitle,gametitlerec)
            if T.winner(board) != None:
                gameover = True
        
        # setting up buttons for game over
        if gameover:
            # back to menu - refreshes whole loop
            menubackbutton = pygame.Rect(150, 500, 300, 50)
            pygame.draw.rect(screen, BACKCOLOR, menubackbutton)
            menutext = smallfont.render("Main Menu", True, MAINCOLOR)
            menurec =  menutext.get_rect()
            menurec.center = menubackbutton.center
            screen.blit(menutext,menurec)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if menurec.collidepoint(mouse):
                    time.sleep(0.2)
                    screen.fill(MAINCOLOR)
                    user = None
                    board = T.initial_state()
                    firstmove = True
                    
    # updates the display
    pygame.display.flip()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    