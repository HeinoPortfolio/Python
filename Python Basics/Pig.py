#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:25:33 2018
@author: ntcrwlr77
"""
import argparse
import random


class Player:
    """ A class to model player attributes"""
    def __init__(self, num_points, player_position):
        """  Initializer of the class
        Args:
            self():
            num_points(int):       initial number of points that each player has
            player_position(int):  player position
        Return:
        Example:
        >>>
        """
        self.number_of_points = num_points
        self.number = player_position + 1

    def addPoints(self, num_points):
        """  Method to add points to player's points
        Args:
            self(Player):    a NetClass object
            num_points(int)   points to be added to the player's points
        Return:
        Example:
        >>> myObj.displayNetClass()
        """
        self.number_of_points = self.number_of_points +  num_points

class Dice:
    """ A class to model the actions and attributes of a die """
    def __init__(self, num_sides):
        """  Initializer of the class
        Args:
            self():
            num_sides(int):       number of sides for the dice
        Return:
        Example:
        >>>
        """
        self.number_of_sides = num_sides

    def rollDie(self):
        """  Method to simulate the roll of a die
        Args:
            self(Dice):    Dice class
        Example:
        >>> rollDie()
        """
        return random.randint(1, self.number_of_sides)

class Pig:
    """ Class to model the game play of a game of Pig"""

    WIN_POINTS = 20
    NEWDIE = Dice(6)

    def displayDirections(self):
        """  Method to display instructions for the game
        Args:
            self(Dice):    Pig class
        Example:
        >>> displayDirections(self)
        """
        print ("*****  Welcome to the game of Pig   *****")
        print ("In this game the objective is to get a score of atleast {}". format(self.WIN_POINTS))
        print ("\nDirections are as follows: \n")
        print ("1) If you roll a 1 you lose your turn.")
        print ("2) If you roll any other number on the die you get those as your points.")
        print ("3) You may roll again or hold and collect whatever points you have accumulated during the turn.")
        print ("4) If you roll a 1 you will lose all points and the next player goes or if you hold you collect your points and the next player goes.")
        print ("5) The game ends when a player reaches or surpasses {}". format(self.WIN_POINTS))
        print (" \n********************************************************************* ")

    def playersTurn(self, player):

        """  Method to perform the player's turn
        Args:
            self(Dice):    Pig class
            player(Player)  Player whose turn it is
        Example:
        >>> playersTurn(self, player)
        """
        player_turn = True
        player_point_count = 0

        print ("\n\nIt is now player {} turn: ".format(player.number))

        while player_turn is True:

            self.displayPlayerPoints(player)
            print ("Total points this turn: {}".format(player_point_count))

            decision = input("Enter h to hold or r to roll: ")
            if decision is 'r':
                #Roll the die
                die_count = self.NEWDIE.rollDie()
                print ("\nThe value of the die roll is: ", die_count)

                if die_count == 1:
                    print ("---> Turn over you loose your points!")
                    print ("-----> You rolled a 1 !!!!")
                    player_turn = False
                else:
                    player_point_count = player_point_count + die_count
                    print ("{} Points will be added to you score.".format(player_point_count))

            elif decision is 'h':
                #print "entered elif."
                player.addPoints(player_point_count)
                self.displayPlayerPoints(player)
                player_turn = False

        print ("---> Your turn is over! \n \t Next Player is rolling.....\n")

    def didPlayerWin(self, player):
        """  Method to check to see if a player won.
        Args:
            selfPig):    Pig class
            player(Player)  Player whose turn it is
        Example:
        >>>didPlayerWin(player)
        """
        if player.number_of_points >= self.WIN_POINTS:
            print ("********* Player Number {} wins this time! ***********".format(player.number))
            return True
        else:
            return False
        #pass

    def displayPlayerPoints(self, player):
        """  Method to display the player's points.
        Args:
            selfPig):    Pig class
            player(Player)  Player whose turn it is
        Example:
        >>>displayPlayerPoints(player)
        """
        print ("--> Player {} has a total point: {}".format(player.number, player.number_of_points))

    def gameStatus(self, playerlst):
        """ Method to display the sttus of the current game and player's
             current totals.
        Args:
            selfPig):    Pig class
            playerlst(list)  Player whose turn it is
        Example:
        >>>gameStatus(playerlst)
        """
        print ("\nCurrent player totals are the following:")

        for index in range(len(playerlst)):

            print ("---> Player {} has a total of: {}  points.  ".format(playerlst[index].number, playerlst[index].number_of_points))

        print ("\n\n")

def main(number_of_players):
    """ Main entry point for the game of Pig
        Args:
            number_of_players(int)  Number of players for the game
        Example:
        >>>main(number_of_players)
    """
    newPig = Pig()
    newPlayerLst = []

    for x in range(0, number_of_players):
        newPlayer = Player(0, x)
        newPlayerLst.append(newPlayer)

    newPig.displayDirections()

    index = 0
    player_win = False

    while player_win is False:

        newPig.playersTurn(newPlayerLst[index])
        player_win = newPig.didPlayerWin(newPlayerLst[index])
        newPig.gameStatus(newPlayerLst)

        if player_win is False:
            if index < (len(newPlayerLst) - 1):
                index += 1
            else:
                index = 0
        else:
            print ("\n\n Game Over!!!!!!!! \n\n")

    #see if the player wants to play again
    playAgain = input("Do you want to play again! Y or N: ")

    if playAgain is 'Y':
        howmanyPlayers = int(input("How many Players do you want? "))
        main(howmanyPlayers)
    elif playAgain is 'N':
        print ("Maybe play later.....good bye.!")
        exit()

if __name__ == "__main__":

    # Retrieve the url from the command line and number of servers.
    PARSER = argparse.ArgumentParser(description="Game of Pig")

    PARSER.add_argument("--numPlayers", metavar='NUMBEROFPLAYERS', type=int, help="Number of Players", required=False)

    args = vars(PARSER.parse_args())

    if args['numPlayers'] is None:
        print ("\nNo number of players given defaulting to 2. \n")
        main(2)
    else:
        main(args['numPlayers'])


