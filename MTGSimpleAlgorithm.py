#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:13:16 2019
@author: Marco Sousa
Subject: Playing with knight deck dmg calculation (MTG)
{

Considerations:
a.) Perhaps this wouldbe better in Java?
b.) Data frame in R?
Building functionality:
1.) Start with just powers and costs
2.) Add on metadata (some abilities)
3.) Add on mana types
Data funconality Qs:
How many turns to win once? How many turns to win MANY on average?
How often do we curve? What ratio is best for ANY MANA TYPE curving? What about correct mana type curving?
JUST land analysis
Likilihood of drawing a color...likilihood to curve w/ versus w/out dual lands...
"""
import numpy as np
import random
#random.shuffle(array)

#Starting with making a turn I can play a single time ONLY focusing on COSTS and POWER:

#The COSTS are for the CMC of the deck
deckCosts = [3,3,3,3,3,3,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#The powers are the respective POWER
deckPowers = [4,4,4,3,3,3,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#deck = [deckCosts, deckPowers]
#Same applies for handCost and handPowers
handCost = []
handPowers = []
#hand = [handCost, handPowers]

turn = 0
mana = 0

lifeTotal = 20
boardPowers = []

#Resets the entire game (all variables).
def resetGame():
    global turn, mana, lifeTotal, boardPowers, deckCosts, deckPowers, handCost, handPowers
    #This is useful at start of new games in succession.
    deckCosts = [3,3,3,3,3,3,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    deckPowers = [4,4,4,3,3,3,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    handCost = []
    handPowers = []
    
    turn = 0
    mana = 0
    
    lifeTotal = 20
    boardPowers = []

#Shuffles the deck.
def shuffleDeck(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

#Draws a card.
def drawCard():
    #Puts the top card into hand
    handCost.append(deckCosts[-1])
    handPowers.append(deckPowers[-1])
    
    #takes one off the deck STACK
    deckCosts.pop()
    deckPowers.pop()
    

def playCard(manaCast):
    """
    Input: Converted Mana Cost of Card.
    Output: pops off the card from hand and adds to board
    Functionality: Note it finds the FIRST index of the given CMC
    """
    
    global mana
    
    cardToPlayIndex = handCost.index(manaCast)
    #play to board
    boardPowers.append(handPowers[cardToPlayIndex])
    #take out of hand
    handCost.pop(cardToPlayIndex)
    handPowers.pop(cardToPlayIndex)
    
    #subtract off the mana of the card
    mana = mana - manaCast


#Can't break right with this
"""
def playCards():
    #Describes the decision tree for choosing WHICH card to play (playCard just plays a GENERAL card)
    
    maxCMC = np.max(handCost)
    minCMC = np.min(handCost)
    
    if (mana == maxCMC):
        
        playCard(maxCMC)
        #mana should be ZERO and work perfectly here
        
    elif(mana > maxCMC):
        
        playCard(maxCMC)
        
        
    elif(mana < maxCMC):
        if(mana in handCost):
            playCard(mana)
    else:
        break
"""
def singleTurn():
    #upkeep
    drawCard()
    
    global turn, mana, lifeTotal
    turn += 1
    mana = turn
    
    #Main Phase
    while(mana > 0):
        #playCards()
        
        maxCMC = np.max(handCost)
    
        if (mana == maxCMC):
        
            playCard(maxCMC)
            #mana should be ZERO and work perfectly here
        
        elif(mana > maxCMC):
        
            playCard(maxCMC)
        
        
        elif(mana < maxCMC):
            if(mana in handCost):
                playCard(mana)
        else:
            break
    
    #attacking Phase
    lifeTotal = lifeTotal - sum(boardPowers)
    #Should improve boardstate in future


def singleSimpleGame():
    
    global turn, lifeTotal
    
    #Starting a new game
    resetGame()
    shuffleDeck(deckCosts, deckPowers)
    
    #drawing seven cards at start of game
    for x in list(range(0,7)):
        drawCard()
    
    #now we implement turns until end (lifetotal = 0)
    while(lifeTotal > 0):
        singleTurn()
    
    
    print(turn, lifeTotal)




singleSimpleGame()






     