with open('input.txt') as input:
    seats = input.read().splitlines()
    
    highest = 0
    
    seatIds = []
    
    for s in seats:
        binaryRep = s.replace('F','0').replace('B','1').replace('L', '0').replace('R','1')
    
        row = int(binaryRep[:7], 2)
        col = int(binaryRep[7:10], 2)
        
        seatId = (row * 8) + col
        seatIds.append(seatId)
        highest = max(highest, seatId)
        
    
    allSeats = set(range(70, highest))
    
    mySeat = allSeats.symmetric_difference(seatIds)
    seatIds.sort()
    print(seatIds)
    print(allSeats)
    print(mySeat)
    
    
    
    
    
    
# get all seat ids from this process.
# generate 0-that number, and then intersect