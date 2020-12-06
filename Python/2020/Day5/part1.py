with open('input.txt') as input:
    seats = input.read().splitlines()
    
    highest = 0
    
    for s in seats:
    
        binaryRep = s.replace('F','0').replace('B','1').replace('L', '0').replace('R','1')
    
        row = int(binaryRep[:7], 2)
        col = int(binaryRep[7:10], 2)
        
        seatId = (row * 8) + col
        highest = max(highest, seatId)
        
    print(highest)