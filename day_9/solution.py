import numpy as np

class Head():
    def __init__(self) -> None:
        self.x = 6
        self.y = 13

    def move(self,where):
        if where == 'R':
            self.x += 1
        elif where == 'L':
            self.x -= 1
        elif where == 'U':
            self.y += 1
        elif where == 'D':
            self.y -= 1

    def position(self):
        return [self.x,self.y]

class Tail():
    def __init__(self) -> None:
        self.x = 6
        self.y = 13

    def is_tail_good(self,head_position):
        a = abs(self.x - head_position[0])
        b = abs(self.y - head_position[1])
        return abs(self.x - head_position[0]) <2 and abs(self.y - head_position[1]) < 2

    def correct_tail(self, where, head_position):
        
        self.x += scale((head_position[0] - self.x))
        self.y += scale((head_position[1] - self.y))

    def position(self):
        return [self.x,self.y]

def scale(num):
        if not -2 < num < 2:
            return num//2
        return num

def main(arg):
    head = Head()
    knots = [Tail() for i in range(8)]
    tail = Tail()

    b_size = 300
    board = np.zeros((b_size,b_size),int)

    if(arg == 1):
        with open("./day_9/data.txt",'r') as move_file:
            for line in move_file:
                move,amount = line.strip('\n').split()
                # print(move,amount)
                board[tail.x,tail.y] = 1
                for i in range(int(amount)):  
                    head.move(move)
                    if not tail.is_tail_good(head.position()):
                        tail.correct_tail(move,head.position())
                    board[tail.x,tail.y] = 1        
    else:
        with open("./day_9/data.txt",'r') as move_file:
            for line in move_file:
                move,amount = line.strip('\n').split()
                # print(move,amount)
                board[tail.x,tail.y] = 1
                
                for i in range(int(amount)):  
                    # print(board,'\n')
                    head.move(move)
                    # board[head.x,head.y] = 1

                    if not knots[0].is_tail_good(head.position()):
                        knots[0].correct_tail(move,head.position())
                    # board[knots[0].x,knots[0].y] = 2

                    for previous_knot,current_knot in zip(knots[:-1],knots[1:]):
                        if not current_knot.is_tail_good(previous_knot.position()):
                            current_knot.correct_tail(move,previous_knot.position())
                        # board[current_knot.x,current_knot.y] = 2

                    if not tail.is_tail_good(knots[7].position()):
                        tail.correct_tail(move,knots[7].position())

                    board[tail.x,tail.y] = 1

                
    print(board.transpose()[::-1, :],'\n')
    print(sum(sum(board)))

if __name__ == "__main__":
    main(2)