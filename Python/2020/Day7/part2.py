import re

def find_contained_bag_count(rules, bag_type):    
    contained_bag_types = []
    
    count = 0
    
    starting_rule = rules[bag_type]
    
    count += sum([a[0] for a in starting_rule])
    count += sum([a[0] * find_contained_bag_count(rules, a[1]) for a in starting_rule])
                
    return count
        

with open('input.txt') as input:
    lines = input.read().splitlines()
    
    rules = {}
    
    for line in lines:
        line_parts = line.split(" bags contain ")
        rule_subject = line_parts[0]
        
        if line_parts[1] == 'no other bags.':
            rules[rule_subject] = []
        else:
            rule_contents = line_parts[1].replace(' bags','').replace(' bag','').replace('.','')
            
            # All this is a bit disgusting, I know
            contained_bags = []            
            for contained_bag in rule_contents.split(','):
                bag_quantity = int(re.search(r'\d+', contained_bag).group())
                contained_bags.append((bag_quantity, ''.join([i for i in contained_bag if not i.isdigit()]).strip()))
                
            rules[rule_subject] = contained_bags
    
    result = find_contained_bag_count(rules, 'shiny gold')
        
    print(result)