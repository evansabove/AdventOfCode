from operator import mul 
from functools import reduce

def get_tree_collisions(rows, x, y):
    xPos = 0
    yPos = 0
    
    treesEncountered = 0
    
    while yPos < len(rows):
        trueXPos = xPos % len(rows[yPos])
        isTree = rows[yPos][trueXPos] == '#'
        
        if isTree:
            treesEncountered += 1
            
        xPos += x
        yPos += y
        
    return treesEncountered
    
with open('input.txt') as input:
    rows = input.read().splitlines()
    
    cases = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    
    for case in cases:
        result = get_tree_collisions(rows, 3, 1)
        
        
    results = [get_tree_collisions(rows, x[0], x[1]) for x in cases]
    
    answer = reduce(mul, results, 1)
    
    
    print(answer)