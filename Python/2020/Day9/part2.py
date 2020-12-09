def is_sum_of_two_items(list, number):
    is_sum_of_previous_items = False
    
    for x in list:
        for y in list:
            if x != y and x+y == number:
                is_sum_of_previous_items = True
                
    return is_sum_of_previous_items

with open('input.txt') as input:
    input = [int(i) for i in input.read().splitlines()]
    
    preamble_length = 25
    preamble = set(input[:preamble_length])
    
    index = 0
    
    invalid_number = 0
    
    while index + preamble_length < len(input):
        is_sum = is_sum_of_two_items(set(input[index:preamble_length + index]), input[preamble_length+index])
        
        if not is_sum:
            invalid_number = input[preamble_length+index]
            break
        
        index += 1
        
    print(invalid_number)
    
    range_start_pos = 0
    range_end_pos = 1
    
    while True:
    
        if sum(input[range_start_pos:range_end_pos]) == invalid_number:
            answer = min(input[range_start_pos:range_end_pos]) + max(input[range_start_pos:range_end_pos])
            print(answer)
            break
            
        elif sum(input[range_start_pos:range_end_pos]) > invalid_number:
            range_start_pos += 1
            range_end_pos = range_start_pos+1
            
        else:
            range_end_pos += 1