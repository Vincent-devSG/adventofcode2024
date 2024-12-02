with open('d2/input.txt') as f:
    input = f.readlines()
    input = [x.strip().split() for x in input]
    input_int = [[int(x) for x in lst] for lst in input]

def part1(input: list) -> int:
    """
    Given a list of lists,
    Find the lists that are sorted in ascending or descending order,
    and the increment between each element is 1, 2, or 3.
    
    Args:
        input: list of lists

    Returns:
        total: int - number of lists that meet the criteria
    """

    accepted_increment = [1, 2, 3]

    total = 0
    for smol_list in input:
        if sorted(smol_list) == smol_list or sorted(smol_list, reverse=True) == smol_list:
            increment = [abs(smol_list[i+1] - smol_list[i]) for i in range(len(smol_list)-1)]
            if all(inc in accepted_increment for inc in increment):
                total += 1
    return total

def part2(input: list) -> int:
    """
    Given a list of lists,
    Find the lists that are sorted in ascending or descending order,
    and the increment between each element is 1, 2, or 3.
    If a list does not meet the criteria, remove one element at a time and check again. Could have used itertools.combinations.
    Could also searched for the i-th element that breaks the criteria and check if the list without i-th or i-th+1 element meets the criteria.

    Args:
        input: list of lists
    
    Returns:
        total: int - number of lists that meet the criteria after removing one element
    """

    total = 0
    accepted_increment = [1, 2, 3]

    def is_valid(smol_list: list) -> bool:
        if sorted(smol_list) == smol_list or sorted(smol_list, reverse=True) == smol_list:
            increment = [abs(smol_list[i+1] - smol_list[i]) for i in range(len(smol_list)-1)]
            if all(inc in accepted_increment for inc in increment):
                return True
    
    for smol_list in input:
        if is_valid(smol_list):
            total += 1
        else:
            for i in range(len(smol_list)):
                if is_valid(smol_list[:i] + smol_list[i+1:]):
                    total += 1
                    break    
    return total



def main():
    print('part1 -> total = ', part1(input_int))
    print('part2 -> total = ', part2(input_int))

if __name__ == "__main__":
    main()