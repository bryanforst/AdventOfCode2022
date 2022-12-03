# A=Rock B=Paper C=Scissors
# X=Rock Y=Paper Z=Scissors
scoring= {
    'AY': 8,
    'AX': 4,
    'AZ': 3,
    'BY': 5,
    'BX': 1,
    'BZ': 9,
    'CY': 2,
    'CX': 7,
    'CZ': 6
}

totalScore = 0
with open("input.txt") as inputFile:
    while True:
        line = inputFile.readline()
        if not line:
            break
            
        thisRound = line.replace(" ","").replace("\n","")
        totalScore += scoring[thisRound]

print(f"Total Score {totalScore}")
  