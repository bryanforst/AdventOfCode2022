total_priority = 0

with open("input.txt") as inputFile:
    while True:
        line = inputFile.readline()
        if not line:
            break
     
        this_napsack = list(line.strip())
        # split into 2 equal parts
        slice_size = int(len(this_napsack) / 2)
        first_part = this_napsack[0: slice_size]
        second_part = this_napsack[slice_size: slice_size*2]
        # find common character
        common_char = [i for i in first_part if i in second_part]
        priority = ord(common_char[0])
        if priority >= 97 :
            priority -= 96
        else:
            priority -= 38
        #print(f"common char {common_char} value {ord(common_char[0])} priority {priority}")
        # calc priority value
        total_priority += priority
       

print(f"Total Priority {total_priority}")
  