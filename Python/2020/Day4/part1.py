with open('input.txt') as input:
    passports = input.read().split("\n\n")
    
    validCount = 0
    
    for p in passports:
        p = p.replace('\n', ' ')
        parts = p.split(' ')
        d = dict(item.split(':') for item in p.split(' '))
        
        mandatoryFields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
        
        if len(mandatoryFields.intersection(d.keys())) == len(mandatoryFields):
            validCount += 1
            
    print(validCount)
        
    
    