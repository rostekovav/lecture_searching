import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open (file_name, "r") as file_obj:
        data = json.load(file_obj)
        return data[field]

def linear_search(sequential_data, number):
    positions = []
    count = 0

    for idx, cislo in enumerate(sequential_data):
        if cislo == number:
            positions.append(idx)
            count += 1

    slovnik = { "positions": positions,
                "count" : count
    }
    return slovnik


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    slovnik_dict = linear_search(sequential_data, 0)
    print(slovnik_dict)


if __name__ == '__main__':
    main()