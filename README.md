# BluePrints-by-Z-Man-Games

# Background:
Blueprints is a game published by Z-Man Games where players build small "buildings" out of 6 dice. There are 4 types of dice, representing different building materials:

black dice (representing stone)
orange dice (representing wood)
clear dice (representing glass)
green dice (representing recycled materials)
Each of these materials score points in different ways...and that's where my code comes in.

Game Tutorial: https://www.youtube.com/watch?v=SEl1Jpdtkd8

# I created a program that:

1. reads in a building from a text file, then
2. writes the score for that building into another text file.

# My Simplifying Assumptions:
As always, simplifying problems by making assumptions is a standard tool in any developer's toolkit.

1. All buildings have 6 dice in them.
2. All buildings consist of 1, 2, or 3 stacks. These stacks are next to each other in a straight line.
3. The text file containing the building to score is called building.txt, is located in a folder called datafiles, and is guaranteed to contain text representing a valid building.
4. The building files have a very specific format - see the following Building File Format section.
5. The only scoring you will need to do is scoring of the materials in the given building - you do not need to worry about the Blueprint Bonus mentioned at the bottom of page 3 of the rules, nor the Awards used in the game.
6. All material scores, and the total score, will be at most 2 digits long.

# Restrictions with the Solution (for best practice):
1. A list of lists must be used to represent a building.
2. The output file must be called scoring-results.txt, be saved in the datafiles folder present in the starting repository, and have a very specific format, which is covered in the section below.
3.  Must have a main() function in a file called asg4.py. 

