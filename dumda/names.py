from random import choice
import sys


def get_names():
    """
    Returns a list of names
    from a text file
    """
    # Open names.txt file to read from and work with
    with open("names.txt", "r") as file:
        # Initialize an empty list to store names
        names = []
        # Iterate through all the names in the text file
        for name in file.readlines():
            # Remove non letter characters and symbols from names
            name = name.rstrip()
            names.append(name)

        return names


def names_by_letter(letter):
    # Open names.txt file to read from and work with
    with open("names.txt", "r") as file:
        # Initialize an empty list to store names
        names = []
        # Iterate through all the names in the text file
        for name in file.readlines():
            # Check if name starts with letter
            if name[0].lower() == letter.lower():
                # Remove non letter characters and symbols from names
                name = name.rstrip()
                names.append(name)

        return names


def get_random_names(names, amount):
    """
    Takes a list of names and an Amount
    and returns a list the length of the given amount of randomly selected names
    """
    # Base Case
    if amount > len(names):
        print(f"there are less than {amount} names in the given list")
        sys.exit(1)

    # Initialize an empty list for storing names
    random_names = []
    # Iterate for the length of the given amount
    for _ in range(amount):
        # Randomly select a name from the list
        name = choice(names)
        random_names.append(name)

    return random_names