class Manager:
    def __init__(self):
        self.tasks = []

    def Add_Task(self, task):
        self.tasks.append(task)

    def Remove_Task(self, index):
        index = int(index)
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Task Not Found")

    def get_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def Get_UnDone(self):
        undone = list(filter(lambda task: task.complete == False, self.tasks))
        print("Incompleted tasks:",undone)

    def Get_Done(self):
        Done = list((filter(lambda task: task.complete == True, self.tasks)))
        print("Completed tasks:",Done)

    def mark_done(self, index):
        index = int(index)
        if 0 <= index < len(self.tasks):
            self.tasks[index].Done()
        else:
            print("Invalid index")


def Auto_register(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        m.Add_Task(self)
    return wrapper

class Task(object):
    @Auto_register
    def __init__(self, title = "title", description = "nothing"):
        self.title = str(title)
        self.description = str(description)
        self.complete = False

    def Done(self):
        print(f"Task {self.title} Done")
        self.complete = True

    def __str__(self):
        return f"Task:{self.title}, description:{self.description}, complete:{self.complete}"
    __repr__ = __str__

m = Manager()
def menu():

    while True:
        global m
        print("==========Welcome to Task Manager Pro==========")
        print("what do you want to do?")
        print("Your current tasks:")
        m.get_tasks()
        print("\n1. Add Task"
              "\n2. Remove Task"
              "\n3. Mark Task as Complete"
              "\n4. Get completed tasks"
              "\n5. Get uncompleted tasks"
              "\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            a = Task(title, description)
        elif choice == "2":
            index = input("Enter task number: ")
            m.Remove_Task(index)
        elif choice == "3":
            index = input("Enter the task number you want to mark: ")
            m.mark_done(index)
        elif choice == "4":
            m.Get_Done()
        elif choice == "5":
            m.Get_UnDone()
        elif choice == "6":
            exit()

menu()









