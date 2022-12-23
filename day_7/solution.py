def open_data(driver: dict):
    with open("./day_7/data.txt",'r') as data_file:
        is_reading_folder = False
        dir = ""
        for line in data_file:
            line = line.strip('\n')
            line = line.strip('/')
            if "$ cd" in line:
                command = line = line.replace("$ cd ","")
                if command == "..":    
                    dir = dir[:dir.rfind('/')] 
                    continue
                else:

                    dir += "/" + line
                driver[dir] = []
                is_reading_folder = False
            elif "$ ls" in line:
                is_reading_folder = True
                continue

            if is_reading_folder:
                if "dir" in line:
                    driver[dir].append(dir + "/" + line.replace("dir ",""))
                else:
                    file_size, *rest = line.split(" ")
                    driver[dir].append(int(file_size))
                continue

def calculate_dir_weight(dir : list, driver : dict) -> int:
    weight = 0
    for element in dir:
        if type(element) is int:
            weight += element
        else:
            weight += calculate_dir_weight(driver[element], driver)
    return weight

def main():
    driver = dict()
    open_data(driver)
    at_most_100_000 = 0
    qualified_for_removal = dict()
    for index,dir in enumerate(driver):
        weight = calculate_dir_weight(driver[dir], driver)
        print(index,dir,weight)
        if weight <= 100_000:
            at_most_100_000 += weight 
    
    needed_space = 30_000_000 - (7e+7 - calculate_dir_weight(driver['/'], driver))
    for dir in driver:
        weight = calculate_dir_weight(driver[dir], driver)
        if weight >= needed_space:
            qualified_for_removal[dir] = weight
        

    print(at_most_100_000)
    min_dir = min(qualified_for_removal, key=qualified_for_removal.get)
    print(min_dir,qualified_for_removal[min_dir])

if __name__ == "__main__":
    main()

    pass