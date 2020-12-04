with open('input.txt') as input:
    rows = input.read().splitlines()
    
    xPos = 0
    yPos = 0
    
    treesEncountered = 0
    
    while yPos < len(rows):
        trueXPos = xPos % len(rows[yPos])
        isTree = rows[yPos][trueXPos] == '#'
        
        if isTree:
            treesEncountered += 1
            
        xPos += 3
        yPos += 1
        
print (treesEncountered)