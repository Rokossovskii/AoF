def download_data(file):
    data = None
    for line in file:
        line = [line[i] for i in range(1,len(line),4)]
        if line[0] == '1':
            return data
        print(line)
        if data == None:
            data = [[] for i in range(len(line))]
        for idx,char in enumerate(line):
            if char != ' ':
                data[idx].insert(0,char)

def moving_crates(line,storage):
    line = line.strip('\n')
    line = line.split(' ')
    for i in range(int(line[1])):
        storage[int(line[5])-1].append(storage[int(line[3])-1].pop())
    
def moving_crates_corectly(line, storage):
    line = line.strip('\n')
    line = line.split(' ')
    buf = []
    for i in range(int(line[1])):
        buf.insert(0,storage[int(line[3])-1].pop())
    storage[int(line[5])-1] += buf

def print_storage(storage):
    name = ""
    for idx,s in enumerate(storage):
        print(idx,s)
        name += s[-1]
    return name
    

with open("day_5/data.txt", 'r') as file:
    storage = download_data(file)

    print_storage(storage)
    file.readline()
    for line in file:
        # moving_crates(line,storage)
        moving_crates_corectly(line,storage)
    
    print(print_storage(storage))


