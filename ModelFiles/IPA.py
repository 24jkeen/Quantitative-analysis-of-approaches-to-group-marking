import numpy

def MakeGroupMatrix(AssignedGroups, n):
    # Create Matrix of correct size populated with zeros
    M = [];
    for i in range(0,n):
        zeros = [0] * n
        M.append(zeros)
    # Fill in matrix with 1 if person is in group
    GroupIndex = 0;
    for Group in AssignedGroups:
        for person in Group:
            M[GroupIndex][person] = 1
        GroupIndex = GroupIndex + 1
    # Transform into a Numpy Matrix and return
    numpy.matrix(M)
    return M

def PrintMatrix(M):
    print("Matrix M:")
    for element in M:
        print(element)

def PiM(GroupMarks, AssignedGroups, n, GroupSize):
    M = MakeGroupMatrix(AssignedGroups, n)
    #PrintMatrix(M)
    PseudoInverse = numpy.linalg.pinv(M)
    #PrintMatrix(PseudoInverse)
    GroupMarks = numpy.matrix(GroupMarks)
    GroupMarks = GroupMarks.getT()
    #PrintMatrix(GroupMarks)
    IndividualMarks = GroupSize * PseudoInverse * GroupMarks
    IndividualMarks = IndividualMarks.flatten()
    IndividualMarks = IndividualMarks.tolist()

    Return = IndividualMarks[0]
    for count in range(len(Return)):
        if Return[count] > 100:
            Return[count] = 100
        elif Return[count] < 0:
            Return[count] = 0
            
    return Return

    
