import re

with open('input.txt') as input:
    instructions = input.read().splitlines()
    
    instruction_record = [(i, 0) for i in instructions]
    
    position = 0
    accumulator = 0
    
    while True:
        
        if instruction_record[position][1] == 1:
            print(accumulator)
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