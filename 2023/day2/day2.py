import os
import numpy as np

CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

@staticmethod
def task1():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    sum_of_ids = 0
    for index, line in enumerate(lines):
        valid_game = True
        game = line.rstrip().split(":")[1].strip(" ")

        hands = game.split(";")
        for hand in hands:
            cubes = hand.strip(" ").split(",")

            for cube in cubes:
                cube = cube.strip(" ").split(" ")
                
                if int(cube[0]) > CUBES[str(cube[1])]:
                    valid_game = False
        if valid_game:
            sum_of_ids += index + 1

    
    print(f"Task 1: {sum_of_ids}")

@staticmethod
def task2():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    total_power = 0
    for _, line in enumerate(lines):
        minimum_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        game = line.rstrip().split(":")[1].strip(" ")

        hands = game.split(";")
        for hand in hands:
            cubes = hand.strip(" ").split(",")

            for cube in cubes:
                cube = cube.strip(" ").split(" ")                
                minimum_cubes[str(cube[1])] = max(int(cube[0]), minimum_cubes[str(cube[1])])

        total_power += np.prod(np.array(list(minimum_cubes.values())))

    
    print(f"Task 2: {total_power}")


if __name__ == "__main__":
    task1()
    task2()
