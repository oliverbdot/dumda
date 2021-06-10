from random import choice
import sys


def get_cities():
    with open('cities.txt', 'r', encoding='utf-8') as f:
        cities = []
        for row in f.readlines():
            city = row.rstrip()
            cities.append(city)

        return cities


def cities_by_letter(letter):
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


def get_random_cities(amount):
    names = get_cities()
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


def get_random_city():
    names = get_cities()

    return choice(names)

