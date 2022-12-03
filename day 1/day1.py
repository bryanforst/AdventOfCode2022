maxEnergy = 0
elfNumber = 0
currentEnergy = 0
allEnergies=[]

with open("input.txt") as inputFile:
    while True:
        line = inputFile.readline()
        # Yes we bail on the last elf
        if not line:
            break
            
        currentLine = line.strip()

        if (not(line and line.strip())):
            allEnergies.append(currentEnergy)
            if(currentEnergy>maxEnergy):
                maxEnergy = currentEnergy

            elfNumber += 1               
            currentEnergy = 0
            
        else:
            currentEnergy += int(line)

print("maxenergy {}".format(maxEnergy))
allEnergies.sort(reverse=True)
print(sum(allEnergies[0:3]))

  