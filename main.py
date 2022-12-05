sections = []
sections_number = []
count = 0

with open("cleaning.txt", "r") as file:
    for line in file:
        sections.append(line)

print(sections)

for item in sections:
    number_1 = int(item.partition("-")[0])
    number_2 = int(item.partition("-")[2].partition(",")[0])
    number_3 = int(item.partition("-")[2].partition(",")[2].partition("-")[0])
    number_4 = int(item.partition("-")[2].partition(",")[2].partition("-")[2].partition("\n")[0])
    sections_number.append((number_1, number_2, number_3, number_4))

print(sections_number)
print(len(sections_number))

for item in sections_number:
    if item[0] <= item[2] and item[1] >= item[3]:
        count = count + 1
    if item[0] >= item[2] and item[1] <= item[3]:
        count = count + 1
    if item[0] == item[2] and item[1] == item[3]:
        count = count - 1

print(count)
