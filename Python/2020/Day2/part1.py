with open('input.txt') as input:
    contents = input.readlines()
    
    validCount = 0
    
    for line in contents:
        parts = line.split(':')
        policy = parts[0]
        password = parts[1].strip()
        
        policy = policy.replace('-',',').replace(' ',',') #repalce all delimiters with commas
        policyParts = policy.split(',')
        minOccurrences = int(policyParts[0])
        maxOccurrences = int(policyParts[1])
        char = policyParts[2]
        
        charCount = password.count(char)
        
        valid = charCount >= minOccurrences and charCount <= maxOccurrences
        
        if(valid):
            validCount += 1
            
print(validCount)