import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now, "now.")

while True:
    user_action = input("Type in Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("Add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("Show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("Edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith("Complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} is done!"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue


    elif user_action.startswith("Exit"):
        break
    else:
        print("command isnt valid bro")

print("Fuck off!")