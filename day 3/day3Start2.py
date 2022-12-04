total_priority = 0
rucksack = []
line_counter = 1

with open("input.txt") as inputFile:
    while True:
        line = inputFile.readline()
        if not line:
            break
            
        rucksack.append( list(line.strip()) )
        # split into 2 equal parts
        if line_counter == 3:
            line_counter = 1
            # find common character
            common_char = [i for i in rucksack[0] if i in rucksack[1] and i in rucksack[2]]
            # calc priority value
            priority = ord(common_char[0])
            if priority >= 97:
                priority -= 96
            else:
                priority -= 38
            #print(f"common char {common_char} value {ord(common_char[0])} priority {priority}")
            total_priority += priority
            rucksack.clear()
        else:
            line_counter += 1

print(f"Total Priority {total_priority}")
  