"""Main Module"""

trees = []
length = 0
width = 0
for l in open("input.txt","rt", encoding="utf8"):
    trees.append(l.strip())
    length += 1
    width = len(l.strip())
    

highest_visibility = 0
for row in range(1,length-1):
    for col in range(1,width-1):

        atree = trees[row][col]
        print(f"row={row} col={col} tree={atree}")
        #top
        top_count = 0
        found=True
        for up in range(row-1,-1,-1):
            top_count +=1
            if atree <= trees[up][col]:
                found=False
                break

        #bottom
        bottom_count = 0
        for down in range(row+1,length):
            bottom_count +=1
            if atree <= trees[down][col]:
                found=False
                break

        #right
        right_count = 0
        found=True
        for right in range(col+1,width):
            right_count +=1
            if atree <= trees[row][right]:
                found=False
                break

        #left
        left_count = 0
        found=True
        for left in range(col-1,-1,-1):
            left_count +=1
            if atree <= trees[row][left]:
                found=False
                break

        tree_visibility = bottom_count*top_count*left_count*right_count
        if tree_visibility > highest_visibility:
            highest_visibility = tree_visibility


print (f" highest visibility= {highest_visibility}")
