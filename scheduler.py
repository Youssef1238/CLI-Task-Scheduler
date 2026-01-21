import time
import  re

class Scheduler : 
    def __init__(self):
        self.tasks = []
    
    def addTask(self, title, delay):
        if not re.match("^[0-9]+$",delay) :
            return False
        self.tasks.append([title , int(delay)])
        return True
    
    def run(self,callback):
        if(len(self.tasks) == 0) : return 0
        self.tasks.sort(reverse=True,key=lambda e : e[1])
        timePassed = 0
        tasks_executed = 0
        while len(self.tasks) != 0 :
            indexes = [i for i, val in enumerate(self.tasks) if val[1] == timePassed]
            if len(indexes) > 0:
                for i in indexes :
                    if callback : callback(self.tasks[i])
                    self.tasks.pop(i)
                    tasks_executed += 1
            time.sleep(1)
            timePassed += 1
        return tasks_executed
        





    





