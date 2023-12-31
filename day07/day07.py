import numpy

dayNumber = "07"
print ("Day {} - Part one !".format(dayNumber))
fichier = open("day{}/input.txt".format(dayNumber), "r")

Lines = fichier.readlines()
result = 0
cards = []

for line in Lines:
    line = line.strip()
    line = line.split(" ")
    line[0] = [x for x in line[0]]
    line[0] = ",".join(line[0])
    line[0] = line[0].replace("T", "10")
    line[0] = line[0].replace("J", "11")
    line[0] = line[0].replace("Q", "12")
    line[0] = line[0].replace("K", "13")
    line[0] = line[0].replace("A", "14")
    line[0] = line[0].split(",")
    line[0] = [int(i) for i in line[0]]
    typeHand = 0

    for i in range(5):
        if line[0].count(line[0][i]) == 5:
            typeHand = 7
            break
        if line[0].count(line[0][i]) == 4:
            typeHand = 6
            break
        if line[0].count(line[0][i]) == 3:
            remaining = line[0].copy()
            remaining = [x for x in remaining if x != line[0][i]]
            if remaining[0] == remaining[1]:
                typeHand = 5
            else :
                typeHand = 4
            break
        if line[0].count(line[0][i]) == 2:
            remaining = line[0].copy()
            remaining = [x for x in remaining if x != line[0][i]]
            assert len(remaining) == 3
            for j in range(3):
                if remaining.count(remaining[j]) == 2:
                    typeHand = 3
                    break
                elif remaining.count(remaining[j]) == 3:
                    typeHand = 5
                    break
                else :
                    typeHand = 2
            break
        typeHand = 1

    cards.append([line[0], int(line[1]), typeHand])

cards = sorted(sorted(cards, key= lambda x: x[0]), key= lambda x: x[2])

result = [(index+1) * card[1] for index, card in enumerate(cards)]
result = sum(result)

print("Result : {}".format(result))

print ("Day {} - Part two !".format(dayNumber))
result = 0

print("Result : {}".format(result))