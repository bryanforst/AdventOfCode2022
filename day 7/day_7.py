"""Main Module"""

cur_dir = []
# [fullname]->[size,parent_dir]
dirs = {}

for l in open("input.txt","rt", encoding="utf8"):
    line = l.strip().split()
    #process command, pop or set current dir
    if l.startswith("$ cd"):
        if line[2] == "..":
            cur_dir.pop()
        else:
            cur_dir.append(line[2])

        # put new folder in directory list along with parent
        parent = '/'.join(cur_dir[:-1])
        dir_name = '/'.join(cur_dir)
        if dir_name not in dirs:
            dirs[dir_name] = [0,parent]

    elif not l.startswith("$ ls") and not l.startswith("dir"):
        # update file size on this and all parents
        s = int(line[0])
        dir_name = '/'.join(cur_dir)
        while dir_name:
            dirs[dir_name][0] += s
            dir_name = dirs[dir_name][1]

total = 0
dir_sizes = []
for size,_ in dirs.values():
    dir_sizes.append(size)
    if size<100000:
        total += size

need = 30000000 - (70000000 - dirs["/"][0])
for size in sorted(dir_sizes):
    if size>need:
        print(f"total={total} largest dir to remove={size}")
        break
