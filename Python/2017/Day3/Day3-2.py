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
    global added_points
    from itertools import cycle
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    added_points = []

    added_points.append((n, pos[0], pos[1]))
    yield n,pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                #if n >= end:
                    #return
                pos = move(*pos)
                #n+=1 # Instead of +1 this is now + all of the surrounding points
                n = get_surrounding_total(*pos)

                if n > 277678:
                    print n
                    return

                added_points.append((n, pos[0], pos[1]))
                yield n,pos

        times_to_move+=1

def get_surrounding_total(x, y):

    surrounding_coordinates = []
    surrounding_coordinates.append((x-1, y)) #Left
    surrounding_coordinates.append((x+1, y)) #Right
    surrounding_coordinates.append((x, y+1)) #Up
    surrounding_coordinates.append((x, y-1)) #Down
    surrounding_coordinates.append((x-1, y+1)) #Top Left
    surrounding_coordinates.append((x+1, y+1)) #Top Right
    surrounding_coordinates.append((x-1, y-1)) #Bottom Left
    surrounding_coordinates.append((x+1, y-1)) #Bottom Right

    return sum([val for val, xPos, yPos in added_points if (xPos,yPos) in surrounding_coordinates])

input = 10
added_points = []

points = gen_points(input)
for i in points:
    print i

print "----------------------------"
print added_points