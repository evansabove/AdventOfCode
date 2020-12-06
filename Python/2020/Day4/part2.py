import re

def passportIsValid(p):
   
    if len(p["byr"]) != 4 or int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
        return False
        
    if len(p["iyr"]) != 4 or int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
        return False
    
    if len(p["eyr"]) != 4 or int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
        return False    
    
    if p["hgt"].endswith("cm"):
        if int(p["hgt"][:-2]) < 150 or int(p["hgt"][:-2]) > 193:
            return False
        
    elif p["hgt"].endswith("in"):
        if int(p["hgt"][:-2]) < 59 or int(p["hgt"][:-2]) > 76:
            return False
    else:
        return False
        
    if not bool(re.match(r"^#([0-9]*[a-f]*){6}$", p["hcl"])):
        return False
        
    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
        
    if not bool(re.match(r"^[0-9]{9}$", p["pid"])):
        return False
        
    return True

with open('input.txt') as input:
    passports = input.read().split("\n\n")
    
    validcount = 0
    
    for p in passports:
        p = p.replace('\n', ' ')
        parts = p.split(' ')
        d = dict(item.split(':') for item in p.split(' '))
        
        mandatoryfields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
        
        if len(mandatoryfields.intersection(d.keys())) == len(mandatoryfields):
            # then the passport is present.
            # but is it valid?
            if passportIsValid(d):
                validcount += 1
            
    print(validcount)