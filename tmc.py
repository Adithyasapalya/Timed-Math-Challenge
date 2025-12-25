import random

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

expr, answer = generate_problem()
print(expr, answer)