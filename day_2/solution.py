# A-Rock
# B-Paper
# C-Scissors

# X-Rock
# Y-Paper
# Z-Scissors

import math

count = 0

with open("day_2/data.txt",'r') as file:
    for line in file:
        round = line.strip('\n').split(' ')
        count += ord(round[1]) - 87 + int((((ord(round[0]) - ord(round[1])+19)/3)*-10)%10)
    print("part one:", count)

count = 0
with open("day_2/data.txt",'r') as file:
    for line in file:
        round = line.strip('\n').split(' ')
        count += (ord(round[1]) - 88)*3 + (ord(round[0]) - 63 + ord(round[1]) - 88)%3 +1
    print("part two:", count)

