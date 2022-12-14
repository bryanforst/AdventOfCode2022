"""Main Module"""

trees = []
length = 0
width = 0
for l in open("input.txt","rt", encoding="utf8"):
    trees.append(l.strip())
    length += 1
    width = len(l.strip())

edge = (width*2) + (length-2)*2
total_visible = edge
for row in range(1,length-1):
    for col in range(1,width-1):

        atree = trees[row][col]

        #top
        found=True
        for up in range(row-1,-1,-1):
            if atree <= trees[up][col]:
                found=False
                break

        if found:
            total_visible += 1
            print("visible from top")
            continue

        #bottom
        found=True
        for down in range(row+1,length):
            if atree <= trees[down][col]:
                found=False
                break

        if found:
            total_visible += 1
            print("visible from bottom")
            continue

        #right
        found=True
        for right in range(col+1,width):
            if atree <= trees[row][right]:
                found=False
                break

        if found:
            total_visible += 1
            print("visible from right")
            continue

        #left
        found=True
        for left in range(col-1,-1,-1):
            if atree <= trees[row][left]:
                found=False
                break

        if found:
            total_visible += 1
            print("visible from left")


print (f" len={length} width={width} edge={edge} visible trees = {total_visible}")
