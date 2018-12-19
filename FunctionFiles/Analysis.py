from math import fabs as absolute
from math import sqrt

def ResultArray(PopArray, CalcArray):
    AbsErrArray = []
    count = 0
    while count < len(PopArray):
        AbsErrArray.append(absolute(CalcArray[count] - PopArray[count]))
        count = count + 1

    MaxErr = max(AbsErrArray)
    AveErr = sum(AbsErrArray) / len(AbsErrArray)

    SqrError = [x**2 for x in AbsErrArray]
    RMS = sqrt(sum(SqrError) / len(SqrError))

    RelErrArray = []
    count = 0
    while count < len(PopArray):
        if PopArray[count] != 0:
            RelErrArray.append((AbsErrArray[count]/PopArray[count])*100)
        count = count + 1
    MaxRelErr = max(RelErrArray)
    AveRelErr = sum(RelErrArray) / len(RelErrArray)

    ResultDict = {"MaxErr": MaxErr,"AveErr": AveErr, "MaxRelErr": MaxRelErr, "AveRelErr": AveRelErr, "RootMeanSqr": RMS, "List": AbsErrArray}
    return ResultDict
    
