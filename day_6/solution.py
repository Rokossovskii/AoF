def find_start_of_packet(string):
    for i in range(4,len(string)):
        if 4 == len(set(string[i-4:i])):
            return i
    else:
        return None

def find_start_of_message(string):
    for i in range(14,len(string)):
        if 14 == len(set(string[i-14:i])):
            return i
    else:
        return None

with open("day_6/data.txt", 'r') as file:
    message = file.readline()
    print(f"Solution to first tasks: {find_start_of_packet(message)}")
    print(f"Solution to second tasks: {find_start_of_message(message)}")
