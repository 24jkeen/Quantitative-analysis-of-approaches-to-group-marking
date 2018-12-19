def Function(Population, GroupArray):
    GroupMarks = []
    index = 0
    for group in GroupArray:
        GroupMarks.append(0)
        for member in group:
            GroupMarks[index] = GroupMarks[index] + Population[member]
        GroupMarks[index] = GroupMarks[index] / len(group)
        index = index + 1
    return GroupMarks
