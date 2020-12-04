with open('input.txt') as input:
    contents = input.readlines()
    
    validCount = 0
    
    for line in contents:
        parts = line.split(':')
        policy = parts[0]
        password = parts[1].strip()
        
        policy = policy.replace('-',',').replace(' ',',') #repalce all delimiters with commas
        policyParts = policy.split(',')
        pos1 = int(policyParts[0])
        pos2 = int(policyParts[1])
        char = policyParts[2]
        
        charCount = password.count(char)
        
        valid = bool(password[pos1-1] == char) ^ bool(password[pos2-1] == char)
        
        if(valid):
            validCount += 1
            
print(validCount)