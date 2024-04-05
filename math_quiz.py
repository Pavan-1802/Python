import random
import time

MIN_OPERAND=3
MAX_OPERAND=12
OPERATORS= ['+','-','*']
MAX_PROBLEMS=10

def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)
    expression=str(left)+operator+str(right)
    answer=eval(expression)
    return expression,answer

input("Press ENTER to start")
start_time=time.time()

for i in range(MAX_PROBLEMS):
    expr,ans=generate_problem()
    while True:
        result=input("Problem No."+str(i+1)+": "+expr+"? ")
        if result==str(ans):
            break

end_time=time.time()
duration=round(end_time-start_time,2)
print(f"You finished in {duration} seconds")