import re
import copy

def program_finishes(instruction_record):

    position = 0
    accumulator = 0
    
    while True:
    
        if position >= len(instruction_record):
            print(accumulator)
            return True
        
        if instruction_record[position][1] == 1:
            return False
            break
            
        instruction_record[position] = (instruction_record[position][0], instruction_record[position][1]+1)
        
        instruction_command = instruction_record[position][0].split(' ')[0]
        instruction_amount = int(instruction_record[position][0].split(' ')[1].replace('+',''))
    
        if instruction_record[position][0][:3] == 'nop':
            position += 1
            continue
            
        if instruction_record[position][0][:3] == 'acc':
            accumulator += instruction_amount
            position += 1
            continue
            
        if instruction_record[position][0][:3] == 'jmp':
            position += instruction_amount
            continue
            
            

with open('input.txt') as input:
    instructions = input.read().splitlines()
    
    instruction_record = [(i, 0) for i in instructions]
    
    replace_position = -1
    
    for instruction in instruction_record:
        replace_position += 1
        
        if instruction[0][:3] == 'acc':
            continue
        elif instruction[0][:3] == 'nop':
            # create copy and replace this position
            c = copy.deepcopy(instruction_record)
            c[replace_position] = (c[replace_position][0].replace('nop','jmp'), c[replace_position][1])
            
            if program_finishes(c):
                print("We're done")
                
        elif instruction[0][:3] == 'jmp':
            # create copy and replace this position
            c = copy.deepcopy(instruction_record)
            c[replace_position] = (c[replace_position][0].replace('jmp','nop'), c[replace_position][1])
            
            if program_finishes(c):
                print("We're done")
                
            
            
    
    
    
    