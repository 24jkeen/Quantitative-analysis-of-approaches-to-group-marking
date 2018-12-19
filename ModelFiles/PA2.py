##Value for being better than someone (should be smaller than b)
a = 0.2
##Value for being worse than someone (should be bigger than a)
b = 1
##Weighting of group mark
z = 0.8
##Weighting of model result
y = 1 - z

import random
import numpy

def CreateRankings(Population, GroupSize):
    # Create matrix with scores in
    ScoreMatrix = CreateBlankMatrix(GroupSize)
    for Member in range(0,GroupSize):
        for Person in range(0,GroupSize):
            # Do not rank themselves
            if Member != Person:
                ScoreMatrix[Member][Person] = Population[Person] + random.randrange(-16, 16)

    # Create a list to store edges of graph
    Edges = []
    PersonIndex = 0
    for row in ScoreMatrix:
        Temp = MakeRowsEdges(row, PersonIndex)
        for edge in Temp:
            Edges.append(edge)
        PersonIndex = PersonIndex + 1

    return Edges

def MakeRowsEdges(row, PersonNumber):
    Edges = []
    for n in range(len(row)):
        if n != PersonNumber:
            for m in range(len(row)):
                if row[n] <= row[m]:
                    if m != n:
                        Edges.append([n, m])
    return Edges

def CreatePRMatrix(Population, GroupSize):
    Rankings = CreateRankings(Population, GroupSize)
    #print(Rankings)

    PRMatrix = CreateBlankMatrix(GroupSize)
    for row_index in range(GroupSize):
        for col_index in range(GroupSize):
            TempValue = 0
            for edge in Rankings:
                if edge == [row_index, col_index]:
                    TempValue = TempValue + a
                elif edge == [col_index, row_index]:
                    TempValue = TempValue + b
            PRMatrix[row_index][col_index] = TempValue
    
    return PRMatrix

"""Works"""
def CreateBlankMatrix(GroupSize):
    PRMatrix = []               ## Page Rank Matrix
    
    for x in range(GroupSize):

        PRMatrix.append([])
        
        for y in range(GroupSize):

            PRMatrix[x].append(0)
    
    return PRMatrix

"""Works"""
def FindMaxEigValAndVec(eigen):
    ReturnList = [0, []]
    Temp = max(eigen[0])
    ReturnList[0] = Temp.real
    for n in range(len(eigen[0])):
        if ReturnList[0] == eigen[0][n]:
            for m in range(len(eigen[1])):
                ReturnList[1].append(eigen[1][m][n])
                
            #ReturnList[1] = eigen[1][n].tolist()
    for index in range(len(ReturnList[1])):
        if ReturnList[1][index].imag == 0:
            ReturnList[1][index] = ReturnList[1][index].real
        if ReturnList[1][index] < 0:
            ReturnList[1][index] = - ReturnList[1][index]
            #print("Index",index, "of the eigenvector is a negative value")
    return ReturnList

def CalculateMarks(GroupSize, GroupMark, EigenVec):
    total = sum(EigenVec)
    Marks = []
    for n in range(len(EigenVec)):
        Marks.append(GroupSize * EigenVec[n] * GroupMark / total)
        if Marks[n] > 100:
            Marks[n] = 100
        elif Marks[n] < 0:
            Marks[n] = 0
    return Marks

        
def PR(Population, GroupSize, GroupMarks, AssignedGroups):
    CalcResultsArray = []
    for n in range(len(Population)):
        CalcResultsArray.append(0)
            
    for GroupIndex in range(len(AssignedGroups)):
        GroupMark = []
        for person in AssignedGroups[GroupIndex]:
            GroupMark.append(Population[person])
        PRMatrix = CreatePRMatrix(GroupMark, GroupSize)
        eigens = numpy.linalg.eig(PRMatrix)
        EigenVec = FindMaxEigValAndVec(eigens)[1]
        Marks = CalculateMarks(GroupSize, GroupMarks[GroupIndex], EigenVec)
        for n in range(len(Marks)):
            Mark = (z * GroupMarks[GroupIndex]) + (y * Marks[n])
            CalcResultsArray[AssignedGroups[GroupIndex][n]] = CalcResultsArray[AssignedGroups[GroupIndex][n]] + (Mark/GroupSize)
    #print(CalcResultsArray)
    return CalcResultsArray
