import sys
from colorama import Fore
import time

tasks = []

def main ():

    argNum = len(sys.argv) - 1
    if(argNum > 0):
        tasks.append([f"{sys.argv[1]}" , int(sys.argv[2])])
        print(f"{Fore.GREEN}Task Added !")
    else :
        print(f"{Fore.RED}no Arguments Provided")


    timePassed = 0
    while len(tasks) != 0 :
        task = tasks[0]
        if(task[1] == timePassed):
            print(f"{Fore.BLUE}[{timePassed}s] : {Fore.WHITE}{task[0]}")
            tasks.pop()
        time.sleep(1)
        timePassed += 1

    print(f"{Fore.GREEN}All Tasks have been executed !")





if __name__ == "__main__":
    main()