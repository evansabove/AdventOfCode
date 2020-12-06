with open('input.txt') as input:
    groupAnswers = input.read().split("\n\n")
    
    yesCount = 0
    
    for group in groupAnswers:
        answers = group.split('\n')
        
        answer_set = set(''.join(answers))
        
        yesCount += len(answer_set)
        
    print(yesCount)