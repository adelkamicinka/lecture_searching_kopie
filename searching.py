from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

import json

def read_data(file_name,field):
    with open("sequential.json", "r", encoding= "utf-8") as file:
        soubor = json.load(file)

    if field not in soubor:
        return None

    with open(file_name, "r", encoding= "utf-8") as file:
        data = json.load(file)

    return data.get(field)

def linear_search(sekvence, cislo):
    positions = []

    for index, value in enumerate(sekvence):
        if value == cislo:
            positions.append(index)

    return {"positions": positions, "count": len(positions)}

def binary_search(sekvence, cislo):
    left = 0
    right = len(sekvence) -1

    while left <= right:
        mid = (left + right) // 2

        if sekvence[mid] == cislo:
            return mid

        elif sekvence[mid] < cislo:
            left = mid + 1

        else:
            right = mid - 1

    return None


def pattern_search()

def main():
        sequential_data = read_data("sequential.json", "unordered_numbers")
        target = 5
        linear_result = linear_search(sequential_data, target)
        print(linear_result)


if __name__ == "__main__":
    main()
