FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """read the todos saved in the saved files and set the save file."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """write new todos."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")