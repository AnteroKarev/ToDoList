import pickle
import datetime
import os

# Creating and loading a dictionary
todofile = 'todo.data'
if not os.path.isfile(todofile):
    todo = {str(datetime.date.today()): ['Your first task']}
    f = open(todofile, 'wb')
    pickle.dump(todo, f)
    f.close()
f = open(todofile, 'rb')
todo = pickle.load(f)
f.close()

# greetings
print('''

                Hi! I'm Casi, your virtual assistant. 
    So far, I'm not very developed, so I live here on the to-do list.
    But I promise that someday my developer, Andy, will make me
                        MUCH BETTER! 
                
                Let me tall you more about my functions:
                
            1) View current to-do list (today)
            2) View cases for a specific date (date)
            3) Adding a task for today (add)
            4) Adding task for a specific date (add_d)
            5) Deleting a task (del)
            6) Deleting a task on a specific date(del_d)
            7) Exit (exit)

                        Productive work!
                        
                            :        :
                            |\______/|
                            | 0 _ 0  |
''')

# start
tsk = input("How can I help? ")

# The program runs until the user types "exit"
while tsk != "exit":

    # function 1
    if tsk == "today":
        day = str(datetime.date.today())
        if day in todo:
            print("Here is the list of tasks for today: ")
            for task in todo[day]:
                print(" - {0}".format(task))
        else:
            print("No tasks for today :)")
        tsk = input("How else I can help? ")

    # function 2
    elif tsk == 'date':
        day = input("Enter the date in the format yyyy-mm-dd: ")
        if not todo[day]:
            print("No tasks for this day :)")
        else:
            print("Here is the list of tasks for this day: ")
            for task in todo[day]:
                print(" - {0}".format(task))
        tsk = input("How else I can help? ")

    # function 3
    elif tsk == "add":
        task = input("What needs to be done? ")
        day = str(datetime.date.today())
        todo[day].append(task)
        f = open(todofile, 'wb')
        pickle.dump(todo, f)
        f.close()
        tsk = input("The task is listed. How else I can help? ")

    # function 4
    elif tsk == 'add_d':
        day = input("Enter the date in the format yyyy-mm-dd: ")
        if day != str(datetime.date.today()):
            todo[day] = []
        task = input("What needs to be done? ")
        todo[day].append(task)
        f = open(todofile, 'wb')
        pickle.dump(todo, f)
        f.close()
        tsk = input("The task is listed. How else I can help? ")

    # function 5
    elif tsk == "del":
        trash = input("Enter the number of the task to be deleted,\nor press 'enter' to completely clear the list. ")
        day = str(datetime.date.today())
        if todo[day]:
            if not trash:
                for i in range(len(todo[day])):
                    del todo[day][i]
                    f = open(todofile, 'wb')
                    pickle.dump(todo, f)
                    f.close()
                    print("List cleared successfully. ")
            else:
                try:
                    print("Task '{0}' deleted successfully.".format(todo[day][int(trash) - 1]))
                    del todo[day][int(trash) - 1]
                except:
                    print("Tasks with this number are not in the list.")
                f = open(todofile, 'wb')
                pickle.dump(todo, f)
                f.close()
        tsk = input("How else I can help? ")

    # function 6
    elif tsk == "del_d":
        day = input("Enter the date in the format yyyy-mm-dd: ")
        trash = input("Enter the number of the task to be deleted,\nor press 'enter' to completely clear the list. ")
        if todo[day]:
            if not trash:
                for i in range(len(todo[day])):
                    del todo[day][i]
                f = open(todofile, 'wb')
                pickle.dump(todo, f)
                f.close()
                print("List cleared successfully. ")
            else:
                try:
                    print("Task '{0}' deleted successfully".format(todo[day][int(trash) - 1]))
                    del todo[day][int(trash) - 1]
                except:
                    print("Tasks with this number are not in the list.")
                f = open(todofile, 'wb')
                pickle.dump(todo, f)
                f.close()
        tsk = input("How else I can help? ")

    # In case of an unexpected command
    else:
        print("Alas, I can't handle it :(")
        tsk = input("How else I can help? ")
print("It was a pleasure to work with you ;)")
