import re

def find_containing_bags(rules, bag_type):    
    containing_bag_types = []
    
    for outer_bag in rules:
        bag_rules = rules[outer_bag]
        
        rule_contains_bag_type = bool([a for a in bag_rules if a[1] == bag_type])
        
        if rule_contains_bag_type:
            containing_bag_types.append(outer_bag)
            
            containing_bags = find_containing_bags(rules, outer_bag)
            
            if containing_bags:
                containing_bag_types.extend(containing_bags)
                
    return containing_bag_types
        

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
    
    result = set(find_containing_bags(rules, 'shiny gold'))
        
    print(len(result))
    
    