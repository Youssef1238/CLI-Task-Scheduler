###### **Description :** 



a script that takes tasks and schedule them.

it works on the CLI.





###### **Conception :**



we need a script that takes two arguments , stores the first as the name of the task and the other as the duration.

error handling should be implemented (input data type , redundancy of a task , input value validation (-1,..) )

if the input is valid the tasks are stored in an object or a dict based on the chosen language.

for now i choose python so we will use a Dict.



research subjects : 



* arguments in python
* scripts running without explicitly using the filename (path ..)
* printing to the cli with colors





so based on the research , the first elemnt in the command changes , if its `add`  we add a task , if its `run` we start running the tasks.

running the task is timed , so we start a timer and whenever the seconds passed match the delay of a task it gets printed , until the tasks dict is empty.

