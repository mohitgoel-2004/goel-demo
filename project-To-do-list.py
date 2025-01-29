#To-Do LIST App in Python

#create an empty list to store all tasks.
task_lst = []

#function to add a task to the list 
def add_task(task):
    task_lst.append(task)
    print(f"Task '{task}' has been added to the list..")

#function to remove a task to the list 
def remove_task(task):
    if task in task_lst:
     task_lst.remove(task)
     print(f"Task '{task}' has been removed to the list..")
    else:
        print(f"Task '{task}' has not found to the list..")

#function to show all tasks io the list
def show_task_lst():
   if task_lst:
      print("Tasks in the To-Do List:")
      for idx, task in enumerate(task_lst, start=1): #enumerate(iterable, start=0)
         print(f"{idx}. {task}")
   else:
       print("The To-Do List is empty..")

#loop control for To-Do List
while True:
   print(''' To-Do List App Menu:
1. Add a task
2. Remove a task
3. Show tasks
4. Quit                                    
''')
   
   choice = input("Enter your choice from (1,2,3 or 4):")

   if choice == '1':
      task = input("Enter the task to add me: ")
      add_task(task)
   elif choice == '2':
       task = input("Enter the task to remove me: ")
       remove_task(task)
   elif choice == '3':
      show_task_lst()
   elif choice == '4': 
      print("Good bye!") 
      break
   else: 
       print("Invalid choice. Please choose any option 1, 2, 3 or 4")