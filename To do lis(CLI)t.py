def dis_menu():
    """......................Displays the menu options............................."""
    print("TO DO LIST MENU.........")
    print("VIEW TASKS:  1")
    print("ADD TASK:  2")
    print("UPDATE TASK:  3")
    print("DELETE TASK  4")
    print("EXIT:  5\n")
def view_task(tasks):
    if tasks:
        print("Your to do list")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")
    else:
        print("No tasks found\n1")
    print("")    
def add_task(tasks):
    task=input("Enter your task: ")
    tasks.append(task)
    print("Task added succesfully...........")
def update_task(tasks):
    view_task(tasks)
    try :
        task_num=int(input("Enter the task num that you want to update: "))
        if (task_num>=1) and (task_num<=len(tasks)):
            new_task=input("Enter your updated task: ")
            tasks[task_num-1]=new_task
            print("updated successfully.........")
        print("Invalid task number")    
    except ValueError:  
        print("Please enter a valid number")
def del_task(tasks):
    view_task()
    try:
        task_num=int(input("Enter task number that you want to delete: "))  
        if (task_num>=1) and (task_num<=len(tasks)):
            deleted_task=tasks.pop(task_num-1)
            print("Task {deleted_task} deleted succesfuly..........")
        else:
            print("Please enter a valid number")
    except ValueError:
        print("Please enter a valid number")
def main():
    tasks=[]
    while True:
        dis_menu()
        choice=int(input("Enter your choice: "))
        if choice==1:
            view_task(tasks)
        elif choice==2:
            add_task(tasks)
        elif choice==3:
            update_task(tasks)
        elif choice==4:
            del_task(tasks)
        elif choice==5:
            print("Exiting the aplication. Have a great day sir.")  
            break
        else:
            print("Enter a valid choice!!!!!!")      
if __name__=="__main__":
    main()            