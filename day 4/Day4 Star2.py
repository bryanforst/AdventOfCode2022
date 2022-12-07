overlaps = 0

with open("input.txt") as inputFile:
    while True:
        line = inputFile.readline()
        if not line:
            break

        assignments = line.strip().split(",")
        assignment1 = assignments[0].split("-")
        assignment2 = assignments[1].split("-")

        if  not (int(assignment1[0])>int(assignment2[1]) or  int(assignment1[1]) < int(assignment2[0])):
            overlaps += 1
            print(f"overlap1 1={assignment1} 2={assignment2}")

        elif not (int(assignment2[0])>int(assignment1[1]) or  int(assignment2[1]) < int(assignment1[0])):
            overlaps += 1
            print(f"overlap2 1={assignment1} 2={assignment2}")


print(f"Total Overlaps {overlaps}")
  