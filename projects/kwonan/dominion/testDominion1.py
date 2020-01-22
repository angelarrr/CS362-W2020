# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 2020

@author: kwonan

Test Scenario #1
"""

from projects.kwonan.dominion import Dominion
from projects.kwonan.dominion import testUtility

# Get player names
player_names = ["*Annie", "*Ben", "*Carla"]

# Construct player objects
players = testUtility.get_players(player_names)

# Initialize the trash
trash = testUtility.init_trash()

# Number of curses and victory cards
nV = testUtility.get_num_victory(player_names)
nC = testUtility.get_num_cursed(player_names)

# Define box
box = testUtility.get_box(20)

# Get supply and supply order
supply = testUtility.get_supply(box, player_names, nV, nC)
supply_order = testUtility.get_supply_order()

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
