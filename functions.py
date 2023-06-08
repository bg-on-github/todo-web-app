FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads the file passed as parameter and
    Returns the list of todos as in the file.
    """
    with open(filepath, 'r') as fil:
        tod = fil.readlines()
    return tod


def write_todos(tods, filepath=FILEPATH):
    """ Writes the list of todos into the file.
    """
    with open(filepath, 'w') as fil:
        fil.writelines(tods)


if __name__ == '__main__':
    print("We are only executing functions.py right now.")
