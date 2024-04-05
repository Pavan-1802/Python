import random

COLORS=['R','G','B','Y','O','W']
NO_OF_TRIES=10
CODE_LENGTH=4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
    
    return code

def guess_code():
    while True:
        guess=input("Guess: ").upper().split(" ")
        if len(guess)!=CODE_LENGTH:
            print(f"Enter exactly {CODE_LENGTH} characters")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color {color}. Enter a new guess")
                break
        else:
            break
    
    return guess

def check_code(real, guess):
    color_counts={}
    correct_pos=0
    incorrect_pos=0

    for color in real:
        color_counts[color]=0
    color_counts[color]+=1

    for r,g in zip(real,guess):
        if r == g:
            correct_pos+=1
            color_counts[g]-=1 
    
    for r,g in zip(real,guess):
        if g in color_counts and color_counts[g]>0:
            incorrect_pos+=1
            color_counts[g]-=1 

    return correct_pos, incorrect_pos   

def game():
    print(f"Welcome to mastermind you have {NO_OF_TRIES} tries")
    print("The valid colors are",*COLORS)
    code=generate_code()

    for attempt in range(NO_OF_TRIES):
        guess=guess_code()
        correct_pos,incorrect_pos=check_code(code,guess)
        if correct_pos==CODE_LENGTH:
            print(f"You have guessed the code in {attempt+1} attempts")
            break
        print(f"{correct_pos} at the correct positions and {incorrect_pos} at the incorrect positions")

    else:
        print("You ran out of tries. The correct code was",*code)

if __name__ == "__main__":
    game()