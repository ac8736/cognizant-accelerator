# task: ("name", "priority", "due date")
# scores: ("name", "score")

tasks = []
scores = []

# function to track tasks
def taskTracking():
    try:
        # get task details
        name = input("Enter the task name: ")
        priorty = int(input("Enter the priority (1 - 10): "))

        # validate input
        if priorty < 1 or priorty > 10:
            raise ValueError
        deadline = input("Enter the deadline (MM/DD/YYYY): ")
        if len(deadline) != 10 or deadline[2] != "/" or deadline[5] != "/" or int(deadline[0:2]) < 1 or int(deadline[0:2]) > 12 or int(deadline[3:5]) < 1 or int(deadline[3:5]) > 31:
            raise ValueError
        task = (name, priorty, deadline)
        tasks.append(task)
        print("Task added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")
    else:
        # sort tasks by priority and then by deadline in descending
        tasks.sort(key=lambda x: (x[1], x[2]), reverse=True)
        print()
        print("Tasks:")
        for task in tasks:
            print(f"   Subject: {task[0]}, Priority: {task[1]}, Deadline: {task[2]}")
    finally:
        print()

# function to track performance
def performanceTracking():
    try:
        # get performance details
        name = input("Enter the name of the subject: ")
        score = float(input("Enter the score (0 - 100): "))

        # validate input
        if score < 0 or score > 100:
            raise ValueError
        score = (name, score)
        scores.append(score)
        print("Score added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")
    else:
        # sort scores by score in descending
        scores.sort(key=lambda x: x[1], reverse=True)
        print()
        print("Subjects in Order of Improvement:")
        for score in scores:
            print(f"   Task: {score[0]}, Score: {score[1]}")
        
        # calculate average score
        avg = 0
        for score in scores:
            avg += score[1]
        print(f"Average Score: {avg / len(scores)}")
    finally:
        print()

def main():
    print("Welcome to the Task and Performance Tracking System!")
    while True:
        # present user with options
        print("Select an option below.")
        print("1. Enter task and View Priorities | 2. Performance Tracking | 3. Exit")
        
        # get user input
        try:
            option = int(input("Enter your choice: "))
            print()

            # perform the selected task
            if option == 1:
                taskTracking()
                print()
            elif option == 2:
                performanceTracking()
            elif option == 3:
                print("Thank you for using the Task and Performance Tracking System!")
                return
            else:
                print("Invalid option. Please try again.")
        except:
            print("Invalid input. Please try again.")


main()
