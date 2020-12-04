with open('input.txt') as input:
    contents = input.readlines()
    
    numbers = [int(x) for x in contents]
    
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020:
                    print(a*b*c)
                    break