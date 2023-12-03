import os
import more_itertools as mit
import numpy as np

CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

@staticmethod
def task1():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    
    lines = [line.rstrip().center(len(line) + 1, ".") for line in lines]

    total_sum = 0
    for row_index, row in enumerate(lines):
        for col_index, col in enumerate(row):
            if col != "." and not col.isdigit():
                rows = lines[row_index - 1:row_index + 2]

                for r in rows:
                    part_number_indices = [i for i in range(len(r)) if r[i].isdigit()]
                    part_number_ranges = [list(group) for group in mit.consecutive_groups(part_number_indices)]

                    for part_number_range in part_number_ranges:
                        if any([x in part_number_range for x in range(col_index - 1, col_index + 2)]):
                            current_sum = int(r[part_number_range[0] : part_number_range[-1] + 1])

                            total_sum += current_sum
    
    print(f"Task 1: {total_sum}")

@staticmethod
def task2():
    with open(CURRENT_FILE_PATH + "/input.txt") as f:
        lines = f.readlines()

    
    lines = [line.rstrip().center(len(line) + 1, ".") for line in lines]

    total_sum = 0
    for row_index, row in enumerate(lines):
        for col_index, col in enumerate(row):
            if col == "*":
                rows = lines[row_index - 1:row_index + 2]

                part_numbers = []
                for r in rows:
                    part_number_indices = [i for i in range(len(r)) if r[i].isdigit()]
                    part_number_ranges = [list(group) for group in mit.consecutive_groups(part_number_indices)]

                    for part_number_range in part_number_ranges:
                        if any([x in part_number_range for x in range(col_index - 1, col_index + 2)]):
                            part_numbers.extend([int(r[part_number_range[0] : part_number_range[-1] + 1])])
                            
                if len(part_numbers) == 2:
                    total_sum += np.prod(part_numbers)

    print(f"Task 2: {total_sum}")

if __name__ == "__main__":
    task1()
    task2()
