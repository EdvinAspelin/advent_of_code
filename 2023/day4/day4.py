import os
import more_itertools as mit
import numpy as np

CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

@staticmethod
def task1():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    total_sum = 0
    for line in lines:
        line = line.split(":")[1].replace("  ", " ")

        current_card, winning_card = tuple(line.strip().split("|"))
    
        current_numbers = list(map(int, current_card.strip().split(" ")))
        winning_numbers = list(map(int, winning_card.strip().split(" ")))

        current_sum = 0
        for number in current_numbers:
            if number in winning_numbers:
                if current_sum == 0:
                    current_sum = 1
                else:
                    current_sum *= 2

        total_sum += current_sum

    print(f"Task 1: {total_sum}")

@staticmethod
def task2():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    winnings = []
    for line in lines:
        line = line.split(":")[1].replace("  ", " ")

        current_card, winning_card = tuple(line.strip().split("|"))
    
        current_numbers = list(map(int, current_card.strip().split(" ")))
        winning_numbers = list(map(int, winning_card.strip().split(" ")))

        current_sum = 0
        for number in current_numbers:
            if number in winning_numbers:
                current_sum += 1

        winnings.append(current_sum)

    scratchcards = [0] * len(winnings)
    for index, winning in enumerate(winnings):
        scratchcards[index] += 1

        if winning != 0:
            scratchcards[index + 1 : index + winning + 1] = list(map(lambda x: x + scratchcards[index], scratchcards[index + 1 : index + winning + 1]))


    print(f"Task 2: {sum(scratchcards)}")

if __name__ == "__main__":
    task1()
    task2()
