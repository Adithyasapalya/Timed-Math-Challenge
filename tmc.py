# A Time based match challenge program, very customizable for different types of arithmetic problems.
import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPS =  3
MAX_OPS =  12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPS, MAX_OPS)
    right = random.randint(MIN_OPS, MAX_OPS)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong=0
input("Press Enter to start!!")
print("-----------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("-----------------------")
print("Nice Work! and You Finished in ", total_time, " seconds!")