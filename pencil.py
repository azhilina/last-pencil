print("How many pencils would you like to use:")
cond = True
while(cond):
    p = input()
    try:
        pencils = int(p)
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if(int(p) < 0):
            print("The number of pencils should be numeric")
        elif((int(p) == 0)):
            print("The number of pencils should be positive")
        else:
            cond = False

print("Who will be the first (John, Jack):")
cond1 = True
while(cond1):
    name1 = input()
    if(name1 not in ["John","Jack"]):
        print("Choose between 'John' and 'Jack'")
    else:
        cond1 = False

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

while (pencils > 0):
    print("{}'s turn:".format(name1))
    cond2 = True
    while(cond2):
        penc = int(input())
        if(penc in ["1","2","3"]):
            cond2 = False
            print("your number is1",penc)
        else:
            print("Too many pencils were taken")
            cond2 = True
            print("your number is2",penc)
    pencils = pencils - penc
    pr(pencils)
    if (pencils > 0):
        print("{}'s turn:".format(name2))
        penc = int(input())
        pencils = pencils - penc
        pr(pencils)

