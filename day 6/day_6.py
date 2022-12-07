"""Main Module"""

my_file= open(r'input.txt', encoding="utf-8")
line = my_file.readline().strip()
length = len(line)
MARKER_LENGTH = 14
my_file.close()

for i in range(length):
    dup_check = set(line[i:i+MARKER_LENGTH])
    if len(dup_check)==MARKER_LENGTH:
        print(f"my marker at {i+MARKER_LENGTH}")
        break
