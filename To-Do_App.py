tasks = []
while True:
    task = input("Enter the task: ")
    tasks.append(task)
    again = input("Add more tasks? (y/n): ")
    if again == "n":
        break

for index, task in enumerate(tasks):
    print(index, tasks)

while True:
    change  = input("Do you want to do any changes in the list? (y/n): ")
    if change == "n":
        break
    elif change == "y":
        choice  = input("What do you want to do?: Delete task or add new task or Replace a task? (Delete/Add)").lower()

        if (choice == "delete"):
            deletion = int(input("Enter the task number you want to delete (state the index of the task): "))

            if type(deletion) != int:
                print("Invalid input")
                exit()
            elif deletion >= len(tasks):
                print("Invalid index")
                exit()
            else:
                del tasks[deletion]
                print("Task deleted successfully")

            for index, task in enumerate(tasks):
                print(index, tasks)

        elif(choice == "add"):
            newtask = input("Entre the new task you want to add: ") 
            tasks.append(newtask) #To add the task
            print("Task added successfully")
            for index, task in enumerate(tasks):
                print(index, tasks)



print("Your final tasks are:\n", tasks)


'''
Mistakes I made in this.
>> I used task but did not made a list before the loop.
>> I forgot the fuctions of list like pop and append.
>> I had made an error in loop formating.
>> I made a mistake in the for loop where is used "tasks" instead of "task" which overlapped my original list and create a string.
>> I used pop instead of del for deletion


'''

