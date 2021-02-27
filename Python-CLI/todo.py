#1.Todo app
"""
1. ./todo list  help
2. ./todo
commands:
-Add
-ls
-del 'Number'
-done 'Number
-help
-report
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
"""
from sys import argv
import os
from datetime import date

def showcase():
    print("""Usage :-
    $ ./todo add "todo item"  # Add a new todo
    $ ./todo ls               # Show remaining todos
    $ ./todo del NUMBER       # Delete a todo
    $ ./todo done NUMBER      # Complete a todo
    $ ./todo help             # Show usage
    $ ./todo report           # Statistics""",end = "") 
def ls(counts):
      if counts == 0:
         print("There are no pending todos!", end ="")
         return
      f = open(path,'r')
      for line in reversed(f.readlines()):
         print('['+' '+str(counts)+']'+line.rstrip())
         counts -=1
      f.close()

def countTodo():
     countTodos = 0
     f = open(path,'r')
     for todo in f:
         countTodos += 1
     f.close()
     return countTodos

def deleteTodo(delTodo):
     f = open(path,'r')
     lines = f.readlines()
     if delTodo == 0:
         print("Error: todo #0 does not exist. Nothing deleted.",end ="")
         return
     try:
         del lines[delTodo-1]
         print(f"Deleted todo #{delTodo}")
         new_todo = open(path,'w+')
         for line in lines:
             new_todo.write(line)
         new_todo.close()
     except:
         print(f"Error: todo #{delTodo} does not exist. Nothing deleted.",end ="")

def doneTodo(dTodo):
     f = open(path,'r')
     lines = f.readlines()
     d = open(currDir+'\done.txt','a+')
     if dTodo == 0:
         print("Error: todo #0 does not exist.",end ="")
         return
     elif dTodo < 0:
         print(f"Error: todo #{dTodo} does not exist.",end = "")
     elif dTodo <= countTodo():    
         d.writelines('x'+" "+today+" "+lines[dTodo-1])
         del lines[dTodo-1]
         new_todo = open(path,'w+')
         for line in lines:
             new_todo.write(line)
         print(f"Marked todo #{dTodo} as done.",end ="")
     else:
          print(f"Error: todo #{dTodo} does not exist.",end = "")

def countDone():
     done = 0
     d = open(currDir+'\done.txt','r')
     for todo in d:
          done += 1
     d.close()
     return done



today = str(date.today())
length = len(argv)
parser = argv
currDir = os.getcwd()
path = currDir+r"/todo.txt"
if length == 1:
    if parser[0] == 'todo.py':
        print(path)
        showcase()
elif length == 2:
    if parser[1] == 'help':
     showcase()
    elif parser[1] =='ls':
     ls(countTodo())
    elif parser[1] =='report':
        done = countDone()
        pending = countTodo()
        print(f"{today} Pending : {pending} Completed : {done}",end = "")
    elif parser[1] =='done':
         print("Error: Missing NUMBER for marking todo as done.",end = "")
    elif parser[1] =="del":
         print("Error: Missing NUMBER for deleting todo.",end ="")
    elif parser[1] =="add":
         print("Error: Missing todo string. Nothing added!",end = "")

elif length == 3:
     if parser[1] == 'add':
         fn = open(path,'a')
         fn.writelines(parser[2]+"\n")
         print(f'Added todo: \"{parser[2]}\"',end = "")
     elif parser[1] == 'del':
         deleteTodo(int(parser[2]))
     elif parser[1] == 'done':
         doneTodo(int(parser[2]))
