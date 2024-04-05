import time

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"
def timer(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed<=seconds:
        time.sleep(1)
        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60
        print(CLEAR_AND_RETURN)
        print(f"{minutes_left:02d}:{seconds_left:02d}")
        time_elapsed+=1

minutes=int(input("Enter the number of minutes: "))
seconds=int(input("Enter the number of seconds: "))
total_time=minutes*60+seconds
timer(total_time)