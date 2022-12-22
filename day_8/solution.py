import numpy as np


def open_data() -> list:
    forest = []

    with open("./day_8/data.txt",'r') as data_file:
        for line in data_file:
            line = [int(x) for x in list(line.strip('\n'))]
            forest.append(line)
    return forest

def check_house_visibility(forest,trees_visibility):
    for times in range(4):
        
        for index_i,forest_row in enumerate(forest):
            highiest_tree = forest_row[0]
            trees_visibility[index_i,0] = 1
            for index_j,j in enumerate(forest_row[1:]):
                if j > highiest_tree:
                    highiest_tree = j
                    trees_visibility[index_i,index_j+1] = 1
                
        forest = forest.transpose()[::-1, :]
        trees_visibility = trees_visibility.transpose()[::-1, :]

def check_visibility_from_house(forest,visibility_from_house):
    for times in range(4):
        for index_i,i in enumerate(forest[1:-1]):
            for index_j,j in enumerate(i[1:-1]):
                house_level = j
                distance = 1
                while(distance + index_j < len(i) - 2 and i[index_j + 1 + distance] < house_level):
                    distance += 1
                visibility_from_house[index_i+1,index_j+1] *= distance
                
        forest = forest.transpose()[::-1, :]
        visibility_from_house = visibility_from_house.transpose()[::-1, :]

def main():
    forest = np.array(open_data())
    trees_visibility = np.zeros(np.shape(forest),dtype=int)
    visibility_from_house = np.ones(np.shape(forest),dtype=int)

    check_house_visibility(forest,trees_visibility)
    check_visibility_from_house(forest,visibility_from_house)
    
    print(forest,'\n')
    print(trees_visibility,'\n')
    print(sum(sum(trees_visibility)))
    print(visibility_from_house,'\n')
    print(np.max(visibility_from_house))

if __name__ == "__main__":
    main()
