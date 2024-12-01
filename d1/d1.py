import numpy as np
# Could have used from collections import Counter, but I wanted to use numpy and default dict

# Read input - Make a numpu array with 2 columns and n rows
with open('d1/input.txt') as f:
    input = f.readlines()
    input = [x.strip().split() for x in input]
    list1 = [int(x[0]) for x in input]
    list2 = [int(x[1]) for x in input]
    formatted_input = np.array([list1, list2])


def part1(input: np.array) -> int:
    """
    Given a 2D numpy array, find the sum of the absolute difference between the two sorted lists

    Args:
        input: 2D numpy array
    
    Returns:    
        result: int - sum of the absolute difference between the two sorted lists
    """

    first_list = np.sort(input[0])
    second_list = np.sort(input[1])
    result = np.sum(np.absolute(first_list - second_list))
    return result

def part2(input: np.array) -> int:
    """
    Given a 2D numpy array, find the number of times each element in the first list appears in the second list.
    Then return the sum of the product of elem[key] with key.

    Args:
        input: 2D numpy array
    
    Returns:
        total: int - sum of the product of elem[key] with key
    """

    first_list = input[0]
    second_list = input[1]

    appeared = {value : 0 for value in first_list}
    total = 0

    for key in appeared.keys():
        appeared[key] = np.count_nonzero(second_list == key)
        total += appeared[key] * key

    return total

def main():
    print('part1 -> total = ', part1(formatted_input))
    print('part2 -> total = ', part2(formatted_input))

if __name__ == "__main__":
    main()
