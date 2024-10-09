def opening_file(filename: str) -> list:
    global dice_building_list
    originalfile = open(filename, "r")
    dice_building_list = []
    for line in originalfile:
        dice_building_list.append(line)
    
    originalfile.close()
    
    return dice_building_list

# Making a 2D list and splitting it into different indexed elements #

def list_2d (full_list: list) -> list:

    if len(dice_building_list) == 2:
        score0 = str(full_list[0]).split('|')
        score1 = str(full_list[1]).split('|')
        total_score = (score0, score1)
        
    elif len(dice_building_list) == 3:
        score0 = str(full_list[0]).split('|')
        score1 = str(full_list[1]).split('|')
        score2 = str(full_list[2]).split('|')
        total_score = (score0, score1, score2)

    elif len(dice_building_list) == 4:
        score0 = str(full_list[0]).split('|')
        score1 = str(full_list[1]).split('|')
        score2 = str(full_list[2]).split('|')
        score3 = str(full_list[3]).split('|')
        total_score = (score0, score1, score2, score3)

    elif len(dice_building_list) == 5:
        score0 = str(full_list[0]).split('|')
        score1 = str(full_list[1]).split('|')
        score2 = str(full_list[2]).split('|')
        score3 = str(full_list[3]).split('|')
        score4 = str(full_list[4]).split('|')
        total_score = (score0, score1, score2, score3, score4)

    elif len(dice_building_list) == 6:
        score0 = str(full_list[0]).split('|')
        score1 = str(full_list[1]).split('|')
        score2 = str(full_list[2]).split('|')
        score3 = str(full_list[3]).split('|')
        score4 = str(full_list[4]).split('|')
        score5 = str(full_list[5]).split('|')

        total_score = (score0, score1, score2, score3, score4, score5)

    list2d = [] 
    for i in range(len(total_score)):
        list2d.append(total_score[i])
         
        
    
    return list2d

# Lists for the scores of Green dice. The index of dice count and score values correspond with each other (i.e. if dice_count[1] = 1 then score_values_g[1]= 2). 

score_values_g = [2,5,10,15,20,30]
dice_count = [1,2,3,4,5,6]

# Calculating the score for the green dice by separating each line into a list and then splitting/indexing each element on the line. 
 
def scoring_green(mainlist: list) -> int:
    scoring_r = 0
    no_dice = 0
    for row in mainlist: 
        for element in row:

# Conditional statement used to check existence of 'R' in any of the elements

            if 'R' in element: 
                no_dice += 1 
    for x in range(6):
        if no_dice == dice_count[x]:
            scoring_r += score_values_g[x]

    return scoring_r

# Calculating the score for clear dice by finding out what the face value is of the dice abbreviated 'G'. #

def scoring_clear (mainlist: list) -> int:
    
    score_g = 0
    face_value_clear = 0
    for i in range(len(mainlist)):
        for j in range(len(mainlist[i])):
            clear_value = (mainlist[i][j])

            if 'G1' in clear_value:
                face_value_clear = 1
            elif 'G2' in clear_value:
                face_value_clear = 2

            elif 'G3' in clear_value:
                face_value_clear = 3
            elif 'G4' in clear_value:
                face_value_clear = 4
            elif 'G5' in clear_value:
                face_value_clear = 5
            elif 'G6' in clear_value:
                face_value_clear = 6
            else:
                face_value_clear = 0

            score_g += face_value_clear

    return score_g

# Calculating the score of black dice by separating each level into specified scores (i.e. level1 = 2pts, level2 = 3pts, level3 = 5, and level4 onwards = 8pts)
# After splitting score levels we multiply and add up occurences of points cummulated from all levels. 

def scoring_black(mainlist: list) -> int:

    level = len(dice_building_list)

    if level < 3:
        
        l1 = dice_building_list[-1].count('S')
        l1_score = (2 * l1)
        l2 = dice_building_list[-2].count('S')
        l2_score = (3 * l2)

        score = l1_score + l2_score

        return score
        
    elif level >= 3:
        if level == 3:
            l1 = dice_building_list[-1].count('S')
            l1_score = (2 * l1)
            l2 = dice_building_list[-2].count('S')
            l2_score = (3 * l2)

            l3 = dice_building_list[-3].count('S')
            l3_score = (5 * l3)
            score = l3_score + l2_score + l1_score

            return score

        elif level == 4:
            l1 = dice_building_list[-1].count('S')
            l1_score = (2 * l1)
            l2 = dice_building_list[-2].count('S')
            l2_score = (3 * l2)
            l3 = dice_building_list[-3].count('S')
            l3_score = (5 * l3)
            l4 = dice_building_list[-4].count('S')
            l4_score = (8 * l4)
            score = l4_score + l3_score + l2_score + l1_score
            return score

        elif level == 5:
            l1 = dice_building_list[-1].count('S')
            l1_score = (2 * l1)
            l2 = dice_building_list[-2].count('S')
            l2_score = (3 * l2)
            l3 = dice_building_list[-3].count('S')
            l3_score = (5 * l3)
            l4 = dice_building_list[-4].count('S')
            l4_score = (8 * l4)
            l5 = dice_building_list[-5].count('S')
            l5_score = (8 * l5)
            score = l5_score + l4_score + l3_score + l2_score + l1_score
            return score
        elif level == 6:  
            l1 = dice_building_list[-1].count('S')
            l1_score = (2 * l1)
            l2 = dice_building_list[-2].count('S')
            l2_score = (3 * l2)
            l3 = dice_building_list[-3].count('S')
            l3_score = (5 * l3)
            l4 = dice_building_list[-4].count('S')
            l4_score = (8 * l4)
            l5 = dice_building_list[-5].count('S')
            l5_score = (8 * l5)      
            l6 = dice_building_list[-6].count('S')
            l6_score = (8 * l6)
            score = l6_score + l5_score + l4_score + l3_score + l2_score + l1_score
            return score

    return score


# Writing function to send written code over to a new file labelled 'scoring.txt' in the specified format. 

def write_score(building_list: list, filename:str, green_score: int, black_score: int, clear_score:int):
    scoring_file = open(filename, "w")
    total_score_file = green_score + black_score + clear_score
    print(*building_list, sep = '\n', file= scoring_file)
    print("\n+----------+----+", file = scoring_file)
    print(f"| glass    |{clear_score:>3} |", file = scoring_file)
    print(f"| recycled |{green_score:>3} |", file = scoring_file)
    print(f"| stone    |{black_score:>3} |", file = scoring_file)
    print("+==========+====+", file = scoring_file)
    print(f"| total    |{total_score_file:>3} |", file = scoring_file)
    print("+----------+----+", file = scoring_file)
    


    scoring_file.close()
    



                
    

# Creating a main function that calls upon all the other functions to display the output in a separate file called scoring.txt. 

def main():
   
    full_list = opening_file("datafiles/building.txt")
    print(full_list, sep = "")
    mainlist = list_2d(full_list)
   
# Print statements to display code output #

    final_green_score = scoring_green(mainlist)
    print("Score for green dice is " , final_green_score)
    final_clear_score = scoring_clear(mainlist)
    print("Score for clear dice is " , final_clear_score)
    final_black_score = scoring_black(mainlist)
    print("Score for black dice is " , final_black_score)
    print("Total Score for all Dice is", final_black_score + final_clear_score + final_green_score)

# Calling upon the write function to create and store values in a new file with specified format #

    write_score(mainlist,"datafiles/scoring-results.txt", final_green_score, final_black_score
    ,final_clear_score)



main()