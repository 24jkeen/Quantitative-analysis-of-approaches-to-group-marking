import random

MarkRatio = 0.7
SelfRatio = 1 - MarkRatio

# Function takes the ideal mark and modifies it randomly
def SelfAssess(RankedStudentMark):
    ReturnMark = RankedStudentMark + random.randrange(-16,16)
    if ReturnMark > 100:
        return 100
    elif ReturnMark < 0:
        return 0
    else:
        return ReturnMark

    # To remove randomness, comment out previous code and uncomment code below
    #return RankedStudentMark

def ReflectiveAccounts1(Population, GroupMarks, AssignedGroups, GroupSize):
    CalcResults = []
    for n in range(len(Population)):
        CalcResults.append(0)
    GroupSize = len(AssignedGroups[0])

    for GroupIndex in range(len(AssignedGroups)):
        Group = AssignedGroups[GroupIndex]
        GroupMark = GroupMarks[GroupIndex]
        for person in Group:
            SelfAssessment = SelfAssess(Population[person])
            Mark = MarkRatio * GroupMark + SelfRatio * SelfAssessment
            CalcResults[person] = CalcResults[person] + Mark / GroupSize        

    return CalcResults

def ReflectiveAccounts2(Population, GroupMarks, AssignedGroups, GroupSize):
    CalcResults = []
    for n in range(len(Population)):
        CalcResults.append(0)
    GroupSize = len(AssignedGroups[0])

    for GroupIndex in range(len(AssignedGroups)):
        Group = AssignedGroups[GroupIndex]
        GroupMark = GroupMarks[GroupIndex]
        SelfAssessList = []
        for person in Group:
            SelfAssessList.append(SelfAssess(Population[person]))
        total = sum(SelfAssessList)
        for index in range(len(SelfAssessList)):
            SelfAssessList[index] = (GroupSize * SelfAssessList[index]) / total
        index = 0
        for person in Group:
            Mark = (MarkRatio + SelfRatio * SelfAssessList[index]) * GroupMark
            CalcResults[person] = CalcResults[person] + Mark / GroupSize
            index = index + 1

    return CalcResults
