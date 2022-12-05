calories_sum_arr = []
count = 0

with open("day_1/data.txt",'r') as file:
    for line in file:
        if line != '\n':
            count += int(line.strip('\n'))
        else:
            calories_sum_arr.append(count)
            count = 0

print(max(calories_sum_arr))


            