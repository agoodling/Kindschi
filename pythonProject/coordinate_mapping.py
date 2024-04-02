

q1,q2,q3,q4 = 0,0,0,0
axis= 0



with open("trial3Coords.txt", "r") as file:
    coordinates = [tuple(map(float, line.strip().split())) for line in file]

count = 0
for cords in coordinates:
    count += 1
    if(cords[0]>0.0 and cords[1] > 0.0):
        q1 += 1
    if (cords[0] < 0.0 and cords[1] > 0.0):
        q2 += 1
    if (cords[0] < 0.0 and cords[1] < 0.0):
        q3 += 1
    if (cords[0] > 0.0 and cords[1] < 0.0):
        q4 += 1
    if(cords[0] == 0.0 or cords[1] == 0.0):
        axis += 1




print(q1,q2,q3,q4,q1+q2+q3+q4+axis,axis,count)