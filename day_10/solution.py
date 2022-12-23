def main():

    data_file = open("./day_10/data.txt",'r')

    signal_strength_cycle = 20
    cycle = 0
    is_calculating = True
    register_x = 1
    value = 0
    signal_sum = 0
    order = ' '
    crt = ''
    
    while(order):
        print(cycle,register_x)
        if cycle == signal_strength_cycle:
                print(">",signal_strength_cycle,register_x)
                signal_sum += register_x*signal_strength_cycle
                signal_strength_cycle += 40
        
        if is_calculating:
            is_calculating = False
            register_x += int(value)
            cycle +=1
        else:
            order = data_file.readline()
            print(order.strip('\n'))
            match order.split(' '):
                case ["addx", value, *rest]:
                    is_calculating = True
                case ["noop"]:
                    pass
            cycle +=1

        if register_x - 1 <= (cycle-1)%40 <= register_x + 1:
            crt += "#"
        else:
            crt += "."

        if cycle%40 == 0:
            crt += '\n'
    print(crt)
    print(signal_sum)

if __name__ == "__main__":
    main()
        