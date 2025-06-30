import datetime
tasks_file="tasks.txt"
def add_task():
    task = input("enter the task you completed today:").strip()
    if not task:
        print("task cannotbe empty")
        return
    date=datetime.date.today().isoformat()
    with open(tasks_file,"a") as file:
        file.write(f"{date} - {task}\n")
    print("task added sucessfully")
def view_task():
    try:
        with open(tasks_file,"r") as file:
            tasks =file.readlines()
            if not tasks:
                print("no task logged yet")
            else:
                print("daily task:\n")
                for line in tasks:
                    print(line.strip())
    except FileNotFoundError:
        print("no task logged yet.start by adding a task ")
def main():
    while True:
        print("\n=== daily task logger===")                            
        print("1.add task")
        print("2.view task")
        print("3.exit")
        choice = input("choose an option(1/2/3):").strip()
        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            print("goodbye")    
            break
        else:
            print("invalid choice.please select 1,2,3.")           
if __name__ =="__main__":
    main()