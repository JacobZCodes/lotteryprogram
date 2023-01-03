import random, time
winner = set()
counter = 0

while True:
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
        winner_list = list(winner)
        break
    else:
        winner.clear()

combination_set = set()
start = time.time()
while True:
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
        counter += 1
        print(combination_list[0], combination_list[1], combination_list[2], combination_list[3], combination_list[4])
        combination_set.clear()
    elif len(combination_list) == 5 and combination_list == winner_list:
        counter += 1
        stop = time.time()
        elapsed_time = stop - start
        print("-" * 40)
        print(f"WINNING NUMBERS: {winner_list[0]} {winner_list[1]} {winner_list[2]} {winner_list[3]} {winner_list[4]}")
        print(f"WE FOUND A MATCH: {combination_list[0]} {combination_list[1]} {combination_list[2]} {combination_list[3]} {combination_list[4]}")
        print(f"This took {counter} tries, and {elapsed_time} seconds!")
        break
    else:
        combination_set.clear()
        continue




