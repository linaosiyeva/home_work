#21 Sticks

#In this game, there are 21 sticks lying in a pile. 
#Players take turns taking 1, 2, or 3 sticks. 
#The last person to take a stick wins. For example:

#Create a robot that will always win the game. 
#Your robot will always go first. 
#The function should take an integer and returns 1, 2, or 3.

#Note: The input will always be valid (a positive integer)

def make_move(sticks):
    return sticks%4
