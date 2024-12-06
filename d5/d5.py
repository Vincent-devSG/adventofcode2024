import re
from collections import defaultdict

with open('d5/test.txt') as f:
    input = f.readlines()
    input = [line.strip() for line in input]
    rule = r'(\d+)\|(\d+)'
    page = r'(\d+)'

    rules = []
    pages = []

    still_rules = True

    for line in input:
        if not line:
            still_rules = False

        if still_rules:
            single_rule = re.findall(rule, line)
            if single_rule:
                rules.append(single_rule)
        
        if not still_rules:
            single_page = re.findall(page, line)
            if single_page:
                pages.append(single_page)

def part1(rules: list, pages: list) -> int:
    """
    Given a list of rules and a list of pages,
    find the number of pages that satisfy the rules.
    
    Args:
        rules: list of rules, X|Y; X should appear before Y
        pages: list of pages, each page is a list of numbers that should satisfy the rules
    
    Returns:
        count: int - number of pages that satisfy the rules
    """
    count = 0

    dict_rules = defaultdict(list)

    for rule in rules:
        dict_rules[rule[0][0]].append(rule[0][1])
    
    break_rule = False
    
    for page in pages:
        break_rule = False
        for i in range(len(page)):       
            if any(rule in page[:i] for rule in dict_rules[page[i]]):
                break_rule = True
        if not break_rule:
            middleIndex = int((len(page) - 1)/2)
            count += int(page[middleIndex])

    return count

def part2(rules: list, pages: list) -> int:
    """
    Given a list of rules and a list of pages,
    find the number of pages that doesn't perfectly satisfy the rules.
    Fix the pages so that they satisfy the rules.
    And find the pages that now satisfy the rules.

    Args:
        rules: list of rules, X|Y; X should appear before Y
        pages: list of pages, each page is a list of numbers that should satisfy the rules
    
    Returns:
        count: int - number of pages that satisfy the rules
    """
    
    count = 0
    dict_rules = defaultdict(list)
    max_looping = 1000

    for rule in rules:
        dict_rules[rule[0][0]].append(rule[0][1])
    
    def verify_page(page):
        break_rule = False
        for i in range(len(page)):       
            if any(rule in page[:i] for rule in dict_rules[page[i]]):
                break_rule = True
        return break_rule

    def fix_page(page):
        for i in range(len(page)):
            for rule in dict_rules[page[i]]:
                if rule in page[:i]:
                    problem = page.index(rule)
                    page[problem], page[i] = page[i], page[problem]
                

    for page in pages:
        if verify_page(page):
            itera = 0
            while verify_page(page) and itera < max_looping:
                fix_page(page)
                itera += 1

            middleIndex = int((len(page) - 1)/2)
            count += int(page[middleIndex])

    return count

def main():
    print('part1 -> total = ', part1(rules, pages))
    print('part2 -> total = ', part2(rules, pages))

if __name__ == '__main__':
    main()