from functools import reduce

with open('input.txt') as input:
    groupAnswers = input.read().split("\n\n")
    
    yesCount = 0
    
    for group in groupAnswers:
        person_answers = group.split('\n')
        
        answer_groups = [list(a) for a in person_answers]
        
        # find the intersection of all these sets
        thing = reduce(set.intersection, [set(x) for x in answer_groups])
        
        yesCount += len(thing)
                
        
    print(yesCount)