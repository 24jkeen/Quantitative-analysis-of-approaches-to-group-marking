from fractions import gcd

def Function(n, GroupSize):

    # check enough n
    if n < GroupSize**2:
        print("There needs to be more people")
        return []

    # Initialise the array to hold the groups in
    GroupArray = []
    i = 0;
    while i < n:
        GroupArray.append([])
        i = i + 1

    # Cycle through until GroupArray is full
    index = 0
    Diff = 1
    while index < len(GroupArray):
        PersonIndex = 0
        i = 0
        while i < n/GroupSize:
            TempArray = [PersonIndex]
            while len(TempArray) < GroupSize:
                PersonIndex = IncreasePersonIndex(PersonIndex, Diff, n)
                TempArray.append(PersonIndex)
            TestUniqueness(TempArray, GroupArray)
            GroupArray[index] = TempArray
            index = index + 1
            i = i + 1
            PersonIndex = IncreasePersonIndex(PersonIndex, Diff, n)
        Diff = NewDiff(Diff, GroupSize, n)

    # Return matrix
    return GroupArray
    

def TestUniqueness(Array, GroupArray):
    for Group in GroupArray:
        if Group == Array:
            print("This does not work")
            return True
    else:
            return False

def IncreasePersonIndex(PersonIndex, Diff, n):
    if PersonIndex + Diff < n:
        return PersonIndex + Diff
##    elif PersonIndex + Diff == n:
##        return PersonIndex + Diff + 1 - n
    else:
        return PersonIndex + Diff - n

def NewDiff(Diff, GroupSize, n):
    if Diff == 1:
        Diff = Diff + GroupSize
        while gcd(Diff, n) != 1:
            Diff = Diff + 1
        return Diff
    else:
        Diff = Diff + 1
        while gcd(Diff, n) != 1:
            Diff = Diff + 1
        return Diff
