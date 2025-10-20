tasks = []
def Menu():
    print("1. Create Task\n2. Change Task\n3. Delite Task\n4. Show Task")
    choice = input("Input User: ")

    match choice:
        case "1":
            print(CreateTask())
        case "2":
            print(ChangeTask())
        case "3":
            print(DeliteTask())
        case "4":
            print(ShowTask())

    return "a0"
def CreateTask():
    task = input("Task: ")
    tasks.append(task)
    return  f"Task Append: {tasks}"



def ChangeTask():
    print("TaskChanged")


def DeliteTask():
    print("TaskDelite")


def ShowTask():
    return tasks





while True:
    print(Menu())

