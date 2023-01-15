import string

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

# function to print the number of pencils in game
def pr(t):
    i = 0
    nums = ""
    while ( i < t ):
        nums = nums + "|"
        i = i + 1
    print(nums)

# function to select correct number of pencils for winning strategy
def decision(a):
    if (int(a) % 4 == 0):
        x = 3
        return x
    elif (int(a) % 4 == 2 or int(a) % 4 == 3):
        x = a % 4 - 1
        return x
    else:
        x = 1
        return x

if (name1 == "John"):
    name2 = "Jack"
elif(name1 == "Jack"):
    name2 = "John"

while (pencils > 0):
    if (name1 == "John"):
        print("John's turn!")
        penc = input()
        while(penc not in ["1","2","3"]):
            print("Possible values: '1', '2' or '3'")
            penc = input()
        while((pencils - int(penc)) < 0):
            print("Too many pencils were taken")
            penc = input()
        pencils = pencils - int(penc)
        pr(pencils)
        winner = name2
        if (pencils > 0):
            print("{}'s turn:".format(name2))
            penc = decision(pencils)
            print(penc)
            pencils = pencils - penc
            pr(pencils)
            winner = name1
    else:
        print("{}'s turn:".format(name1))
        penc = decision(pencils)
        print(penc)
        pencils = pencils - penc
        pr(pencils)
        winner = name2
        if (pencils > 0):
            print("John's turn!")
            penc = input()
            while(penc not in ["1","2","3"]):
                print("Possible values: '1', '2' or '3'")
                penc = input()
            while((pencils - int(penc)) < 0):
                print("Too many pencils were taken")
                penc = input()
            pencils = pencils - int(penc)
            pr(pencils)
            winner = name1
            
print("{} won!".format(winner))

