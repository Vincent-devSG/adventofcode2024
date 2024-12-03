import re

with open('d3/input.txt') as f:
    input = f.readlines()

def part1(input: list) -> int:
    """
    Given a list of strings,
    find all the instances of mul(a,b), where a and b are \d{1,3}
    and return the sum of the product of a and b.

    Args:
        input: list of strings
    
    Returns:
        count: int - sum of the product of a and b
    """
    count = 0
    for line in input:
        mult = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        for elem in mult:
            count += int(elem[0]) * int(elem[1])
    
    return count

def part2(input: list) -> int:
    """
    Given a list of strings,
    find all the instances of mul(a,b), where a and b are \d{1,3}, and do() is stated beforehand.
    Any mul(a,b) after don't() is ignored.
    Return the sum of the product of a and b.

    Args:
        input: list of strings
    
    Returns:    
        count: int - sum of the product of a and b
    """
    count = 0
    big_line = ''

    for line in input:
        big_line += line
    
    big_line = 'do()' + big_line + 'don\'t()'

    do_pattern = r'do\(\)(.*?)(?=don\'t\()'
    do_match = re.findall(do_pattern, big_line)

    for elem in do_match:
        mult = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', elem)
        for elem in mult:
            count += int(elem[0]) * int(elem[1])
            
    return count
    
def main():
    print('part1 -> total = ', part1(input))
    print('part2 -> total = ', part2(input))


if __name__ == "__main__":
    main()
