#make a todo list including input

todo_list = []
while True:
    action = input("Type add, show, edit, complete, or exit: ").lower()
    if action == "add":
        todo = input("Enter a to-do: ")
        todo_list.append(todo)
    elif action == "show":
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")
    elif action == "edit":
        try:
            number = int(input("Number of the todo: "))
            todo = input("Enter a to-do: ")
            todo_list[number - 1] = todo
        except IndexError:
            print("Invalid number.")
    elif action == "complete":
        try:
            number = int(input("Number of the todo: "))
            todo_list.pop(number - 1)
        except IndexError:
            print("Invalid number.")
    elif action == "exit":
        break

#print the todo list
if len(todo_list) > 0:
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item}")
else:
    print("Your todo list is empty.")

#print the number of todos
print(f"You have {len(todo_list)} todos.")







