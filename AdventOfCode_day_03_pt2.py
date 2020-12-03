# Day 03, 2020
# Toboggan Trajectory

def read_input():
    data = open('Input_day_03.txt','r')
    #data = open('test_day_03.txt','r')
    grid_map = [[ch for ch in line.rstrip()] for line in data]
    data.close()
    return grid_map


def print_map(grid_map):
    for line in grid_map:
        print(''.join(line))


def find_height(grid_map):
    return len(grid_map)


def find_width(grid_map):
    return len(grid_map[0])


def count_trees(grid_map, step_x, step_y, start, height, width):
    position_x = start[0]
    position_y = start[1]
    count = 0

    while position_y < height:
        if grid_map[position_y][position_x] == '#':
            count = count + 1
        position_x = (position_x + step_x)%(width)
        position_y = position_y + step_y

    return count


def main():
    grid_map = read_input()
    #print_map(grid_map)

    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    start = [0,0]
    height = find_height(grid_map)
    width = find_width(grid_map)

    total_count = 1 

    for slope in slopes:
        
        count = count_trees(grid_map, slope[0], slope[1], start, height, width)
        print('Count for slope x = '+str(slope)+', y = '+str(slope[1])+' is: '+str(count))
        #total_count = total_count*count
        total_count *= count
        print('Total count is: '+str(total_count)+'\n')

    print('Total count is: '+str(total_count))
    

if __name__ == "__main__":
    main()
