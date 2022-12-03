# A=Rock B=Paper C=Scissors
# X=Lose Y=Draw Z=Win
scoring= {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7
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
  