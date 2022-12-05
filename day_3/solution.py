count = 0

with open("day_3/data.txt",'r') as file:
    for line in file:
        line = line.strip('\n')
        common = list(set(line[:len(line)//2]) & set(line[len(line)//2:]))
        
        if common[0].islower():
            count += ord(common[0]) - 96
        else:
            count += ord(common[0]) - 38
    print("first part",count)

count = 0

with open("day_3/data.txt",'r') as file:
    group_of_three = []
    for idx, line in enumerate(file):
        group_of_three.append(line.strip('\n'))
        if (idx+1)%3:
            pass
        else:
            common = list(set(group_of_three[0]) & set(group_of_three[1]) & set(group_of_three[2]))
            group_of_three = []
            if common[0].islower():
                count += ord(common[0]) - 96
            else:
                count += ord(common[0]) - 38
    print("second part",count)