"""Sam Sheppard"""


name = input(str("What is your name? "))
while name == "":
    print("That is not valid")
    name = input(str("What is your name? "))
AlternateName = " "
for i in range(len(name)):
    if (i % 2) == 0:
        AlternateName += name[i]
print(AlternateName)
