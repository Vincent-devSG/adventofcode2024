import re
with open('d4/input.txt') as f:
    input = f.readlines()
    input = [line.strip() for line in input]

def part1(input: list) -> int:
    """
    Given a list of strings,
    find all the instances of XMAS and SAMX in the rows, columns and diagonals of the matrix.
    Return the count of XMAS and SAMX.

    Args:
        input: list of strings
    
    Returns:
        count: int - count of XMAS and SAMX
    """
    xmas = r'XMAS'
    samx = r'SAMX'
    count = 0

    for line in input:
        xmas_count = re.findall(xmas, line)
        samx_count = re.findall(samx, line)
        count += len(xmas_count) + len(samx_count)
    
    input_col = input

    input_col = list(map(list, zip(*input_col)))
    input_col = [''.join(line) for line in input_col]
    for line in input_col:
        xmas_count = re.findall(xmas, line)
        samx_count = re.findall(samx, line)
        count += len(xmas_count) + len(samx_count)
    
    diag_list = []
    input_diag = input
    x, y = len(input_diag), len(input_diag[0])

   # From top-left to bottom-right
    for i in range(x):
        diag_list.append(''.join([input_diag[i+j][j] for j in range(min(x-i, y))]))
    for i in range(1, y):  # Start from second column
        diag_list.append(''.join([input_diag[j][i+j] for j in range(min(y-i, x))]))

    # From bottom-left to top-right
    for i in range(x):
        diag_list.append(''.join([input_diag[i-j][j] for j in range(min(i+1, y))]))
    for i in range(1, y):  # Start from second column
        diag_list.append(''.join([input_diag[x-1-j][i+j] for j in range(min(y-i, x))]))
        
    for line in diag_list:
        xmas_count = re.findall(xmas, line)
        samx_count = re.findall(samx, line)
        count += len(xmas_count) + len(samx_count)

    return count

def part2(input: list) -> int:
    """
    Given a list of strings,
    find all the instances of : an X shape of the word 'MAS'.  So it should look like this:
    M.S
    .A.
    M.S

    Return the count of such X shapes.

    Args:
        input: list of strings
    
    Returns:
        count: int - count of X shapes
    """
    
    x, y = len(input), len(input[0])
    count = 0

    for i in range(x):
        for j in range(y):
            if input[i][j] == 'A':
                
                # Check left-top corner - and bottom-right corner
                if ((i-1 >= 0 and j-1 >= 0 and input[i-1][j-1] == 'S') and (i+1 < x and j+1 < y and input[i+1][j+1] == 'M')) \
                    or ((i-1 >= 0 and j-1 >= 0 and input[i-1][j-1] == 'M') and (i+1 < x and j+1 < y and input[i+1][j+1] == 'S')):

                    # now check right-top corner - and left-bottom corner
                    if ((i-1 >= 0 and j+1 < y and input[i-1][j+1] == 'S') and (i+1 < x and j-1 >= 0 and input[i+1][j-1] == 'M')) \
                        or ((i-1 >= 0 and j+1 < y and input[i-1][j+1] == 'M') and (i+1 < x and j-1 >= 0 and input[i+1][j-1] == 'S')):
                        count += 1
    
    return count

def main():
    print('part1 -> total = ', part1(input))
    print('part2 -> total = ', part2(input))

if __name__ == '__main__':
    main()