def SOPP(GroupMarks, AssignedGroups, n):
    CalcResults = []
    for x in range(0,n):
        CalcResults.append(0)

    counter = 0
    for group in AssignedGroups:
        mark = GroupMarks[counter]
        for person in group:
            CalcResults[person] = CalcResults[person] + (mark / len(group))
        counter = counter + 1

    return CalcResults
    
