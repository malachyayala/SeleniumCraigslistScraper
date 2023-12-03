import re
file = "postingInfo.txt"
with open(file, 'r') as file:
    elements = [line.strip() for line in file.readlines()]
data = elements
dataCopy = []
digits = []
pattern = re.compile(r'\b\d{2}\b')

for i in data:
    if "hour" in i.split("·")[1] or "hr" in i.split("·")[1]:
        dataCopy.append(i.split("·"))
for i in dataCopy:
    match = pattern.search(i[1])
    if match:
        two_digits = match.group()
        digits.append([i[0], two_digits])

print(dataCopy)
print("********************")
print(digits)