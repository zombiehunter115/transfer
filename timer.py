import time
def countDownTimer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs = int(seconds % 60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds-=1
    print("Time Up")
seconds = input("enter the time in number of seconds")
countDownTimer(int(seconds))        
