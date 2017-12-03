def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

moves = [move_right, move_up, move_left, move_down]

def gen_points(end):
    from itertools import cycle
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    yield n,pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n+=1
                yield n,pos

        times_to_move+=1

def manhattan_distance(sx, sy, ex, ey):
    return abs(ex - sx) + abs(ey - sy)

input = 277678

for i in gen_points(input):
	if i[0] == input:
		print i[1]
		print manhattan_distance(i[1][0], i[1][1], 0, 0)


