import random, time
winner = set()
# Winner initialized as a set to prevent duplicates from being rolled.
# This is meant to mimic the real world lottery where duplicates are 
# not allowed.
counter = 0

while True:
    # Rolls five balls that subsequent rolls need to match up to
    # in order to win.
    ball_1 = random.randint(1,40)
    winner.add(ball_1)
    ball_2 = random.randint(1,40)
    winner.add(ball_2)
    ball_3 = random.randint(1,40)
    winner.add(ball_3)
    ball_4 = random.randint(1,40)
    winner.add(ball_4)
    ball_5 = random.randint(1,40)
    winner.add(ball_5)
    
    if len(winner) == 5:
        # If winner's length is equal to five, winner now contains five balls, none of which are duplicates
        # (since winner is initialized as a set). This will be the five numbers that subsequent ball
        # rolls need to match up to in order to win.
        winner_list = list(winner)
        break
    
    else:
        # If winner's length is not equal to five, that means the program did its job - winner, being a set,
        # removed duplicate values. Since there is now less than five balls in winner, the while-loop
        # needs to be run again until winner's length is five (no duplicate numbers).
        winner.clear()

combination_set = set()
start = time.time()

while True:
    # Rolls 5 balls each with a range of 1-40.
    ball_1 = random.randint(1,40)
    combination_set.add(ball_1)
    ball_2 = random.randint(1,40)
    combination_set.add(ball_2)
    ball_3 = random.randint(1,40)
    combination_set.add(ball_3)
    ball_4 = random.randint(1,40)
    combination_set.add(ball_4)
    ball_5 = random.randint(1,40)
    combination_set.add(ball_5)
    combination_list = list(combination_set)
    
    if len(combination_list) == 5 and combination_list != winner_list:
        # This if-statement executes for an incorrect roll of 
        # five non-duplicate balls.
        counter += 1
        print(combination_list[0], combination_list[1], combination_list[2], combination_list[3], combination_list[4])
        combination_set.clear()
    
    elif len(combination_list) == 5 and combination_list == winner_list:
        # This elif-statement executes when a match has been found.
        counter += 1
        stop = time.time()
        elapsed_time = stop - start
        print("-" * 40)
        print(f"WINNING NUMBERS: {winner_list[0]} {winner_list[1]} {winner_list[2]} {winner_list[3]} {winner_list[4]}")
        print(f"WE FOUND A MATCH: {combination_list[0]} {combination_list[1]} {combination_list[2]} {combination_list[3]} {combination_list[4]}")
        print(f"This took {counter} tries, and {elapsed_time} seconds!")
        break
    
    else:
        # Again, duplicates in each 5-ball roll need to eliminated. This else-statement
        # executes if duplicates were rolled; <5 ball rolls are not counted 
        # and thus counter's value will not be altered.
        combination_set.clear()
        continue




