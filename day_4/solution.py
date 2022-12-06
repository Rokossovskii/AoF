subsets = 0
overlaps = 0

def is_subset(line):

    first,second = line.strip('\n').split(',')
    first,second = first.split('-'),second.split('-')
    set_one = {x for x in range(int(first[0]),int(first[-1])+1)}
    set_two = {x for x in range(int(second[0]),int(second[-1])+1)}
    if len(set_one) < len(set_two):
        return set_one.issubset(set_two)
    else:
        return set_two.issubset(set_one)

def is_overlap(line):
    first,second = line.strip('\n').split(',')
    first,second = first.split('-'),second.split('-')
    set_one = {x for x in range(int(first[0]),int(first[-1])+1)}
    set_two = {x for x in range(int(second[0]),int(second[-1])+1)}
    if set_one.intersection(set_two):
        return True
    else:
        return False

with open("day_4/data.txt") as file:
    for line in file:
        if is_subset(line):
            subsets += 1
        if is_overlap(line):
            overlaps += 1
    
    print("subsets:", subsets)
    print("overlaps:", overlaps)