pencils = int(input("How many pencils would you like to use: \n"))
name1 = input("Who will be the first (John, Jack): \n")
i = 0
nums = ""
while ( i < pencils ):
    nums = nums + "|"
    i = i + 1
print(nums)

def pr(t):
    i = 0
    nums = ""
    while ( i < t ):
        nums = nums + "|"
        i = i + 1
    print(nums)


if (name1 == "John"):
    name2 = "Jack"
elif(name1 == "Jack"):
    name2 = "John"

while (pencils != 0):
    print("{}'s turn:".format(name1))
    penc = int(input())
    pencils = pencils - penc
    pr(pencils)
    if (pencils > 0):
        print("{}'s turn:".format(name2))
        penc = int(input())
        pencils = pencils - penc
        pr(pencils)

# print("{}'s turn:".format(name1))
# print("{}'s turn:".format(name2))
