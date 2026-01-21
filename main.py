from colorama import Fore
from scheduler import Scheduler

Sc = Scheduler()

def main ():

    Running = True

    while Running :
        command = input(f"\n{Fore.WHITE}> ")
        args = command.split(" ")

        if len(args) == 0: 
            continue 

        if len(args) == 1 :
            if args[0] == "run" :
                executed = Sc.run(task_executer)
                if  executed == 0 :
                    print(f"{Fore.YELLOW}There is no tasks to be executed !")
                else :
                    print(f"{Fore.GREEN}All {executed} Tasks have been executed !") 

            elif args[0] == "quit" : 
                Running = False
                print(f"{Fore.BLUE}Session Closed !")

            else : 
                Help()
                
        elif len(args) == 3 and args[0] == "add":
            if not Sc.addTask(args[1] , args[2]):
                Help()
        else :
            Help()




def task_executer(task):
    print(f"{Fore.BLUE}[{task[1]}s] : {task[0]}")

def Help():
    print(f"{Fore.BLUE}Usage : {Fore.WHITE} add <task title> <delay>")
    print(f"        {Fore.WHITE} run")
    print(f"        {Fore.WHITE} quit")
    





if __name__ == "__main__":
    main()