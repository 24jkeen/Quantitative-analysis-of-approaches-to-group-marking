import random

# Function takes the ideal mark and modifies it randomly
def StudentRanking(RankedStudentMark):
    ReturnMark = RankedStudentMark + random.randrange(-16,16)
    if ReturnMark > 100:
        return 100
    elif ReturnMark < 0:
        return 0
    else:
        return ReturnMark

    # To remove randomness, comment out previous code and uncomment code below
    #return RankedStudentMark

def CalculateNormalisedMark(OpinionMarks, index):
    NormalisedMark = 0

    for person in OpinionMarks:
        Total = sum(list(person))
        if Total != 0:
            NormalisedMark = NormalisedMark + (person[index] / Total)
        else:
            NormalisedMark = 0

    return NormalisedMark

def IndividualMark(Multiplier, GroupMark):
    Mark = Multiplier * GroupMark
    if Mark > 100:
        return 100
    elif Mark < 0:
        return 0
    else:
        return Mark
    

def SingleGroupPA(IdealMarks, GroupMark):
    # Initialise variables
    GroupSize = len(IdealMarks)
    OpinionMarks = []
    ModelMarks = []
    # Let each student decide the others marks
    for index in range(0,GroupSize):
        OpinionMarks.append([])
        for count in range(0,GroupSize):
            OpinionMarks[index].append(0)
            if count != index:
                OpinionMarks[index][count] = StudentRanking(IdealMarks[count])
    #print(OpinionMarks)
    # Normalise each persons mark
    for n in range(0, len(OpinionMarks)):
        Multiplier = CalculateNormalisedMark(OpinionMarks, n)
        Mark = IndividualMark(Multiplier, GroupMark)
        ModelMarks.append(Mark)

    return ModelMarks

def NPA(Population, GroupMarks, AssignedGroups, GroupSize):
    # Work out how many different projects there are
    NumberOfGroups = int( len(Population) / GroupSize )
    Projects = int( len(GroupMarks) / NumberOfGroups )
    
    # Create a list to store each persons mark
    PopCalcMarks = []
    Test = []
    for n in range(len(Population)):
        PopCalcMarks.append(0)
        Test.append(0)
        
    # Cycle through each group
    for GroupNumber in range(0,len(GroupMarks)):
        # Get each piece of information needed
        GroupIdealMarks = []
        ReverseIndex = AssignedGroups[GroupNumber]
        for PersonIndex in AssignedGroups[GroupNumber]:
            GroupIdealMarks.append(Population[PersonIndex])
        GroupMark = GroupMarks[GroupNumber]
        # Run model on individual group
        CalcMarks = SingleGroupPA(GroupIdealMarks, GroupMark)
        # Assign the marks
        for count in range(len(CalcMarks)):
            NormalisedMark = CalcMarks[count] / Projects
            PopCalcMarks[ReverseIndex[count]] = PopCalcMarks[ReverseIndex[count]] + NormalisedMark
    return PopCalcMarks
