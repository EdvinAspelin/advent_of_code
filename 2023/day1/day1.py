import os

CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

NUMBERS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

@staticmethod
def get_first_integer(symbols):
    for symbol in symbols:
        if symbol.isdigit():
            return int(symbol)
    
    raise Exception("No integer in symbols")

@staticmethod
def task1():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    total_sum = 0
    for line in lines:
        symbols = [*line]

        first_integer = get_first_integer(symbols)
        symbols.reverse()
        last_integer = get_first_integer(symbols)

        total_sum += 10 * first_integer + last_integer
        
    print(f"Task 1: {total_sum}")

@staticmethod
def get_significant_integer(line, comparator):
    # (index, value)
    found_number = (None, None)
    for number in list(NUMBERS.keys()) + list(NUMBERS.values()):
        first_index = line.find(str(number))
        last_index = line.rfind(str(number))
        
        if comparator(last_index, first_index):
            index = last_index
        else:
            index = first_index

        if index >= 0:
            if found_number[0] is None or comparator(index, found_number[0]):
                if isinstance(number, str):
                    found_number = (index, NUMBERS[number])
                else:
                    found_number = (index, number)
    return found_number[1]

@staticmethod
def task2():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    greater_than = lambda a, b : a > b
    lesser_than = lambda a, b : a < b

    total_sum = 0
    for line in lines:
        first_integer = get_significant_integer(line, lesser_than)
        last_integer = get_significant_integer(line, greater_than)

        total_sum += 10 * first_integer + last_integer
        
    print(f"Task 2: {total_sum}")


if __name__ == "__main__":
    task1()
    task2()
