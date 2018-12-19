# Import standard python modules needed
import sys
import os
import matplotlib.pyplot as plt

#Import addition function files
sys.path.append(os.getcwd() + "\ModelFiles")
sys.path.append(os.getcwd() + "\FunctionFiles")

import Population
import AssignGroup
import CalculateGroupMarks
import Analysis

from RA import ReflectiveAccounts1
from RA import ReflectiveAccounts2
from IPA import InverseProblemApproach
from PA1 import PeerAssessment1
from PA2 import PeerAssessment2
from SOPP import SelfOrganisedPeerPressure

def PrintFormattedList(List):
    FormattedList = ['%.1f' % elem for elem in List]
    print([float(elem) for elem in FormattedList])

def PrintResults(Results):
    if Results == []:
        return
    #PrintFormattedList(Results["List"])
    print("Maximum error is: ",'%.1f' %Results["MaxErr"])
    print("Average error is: ", '%.1f' %Results["AveErr"])
    print("Maximum Relative error is: ",'%.1f' %Results["MaxRelErr"]+"%")
    print("Average Relative error is: ", '%.1f' %Results["AveRelErr"]+"%")
    print("Root mean squared error is: ", '%.1f' %Results["RootMeanSqr"])

def SingleModelWithPrint(n,GroupSize,Model):
    # Population Function
    PopList = Population.Function(n)
    print("Population")
    print(PopList)

    # Assign Groups
    AssignedGroups  = AssignGroup.Function(n, GroupSize)
    print("\nGroupings")
    print(AssignedGroups)

    # Calculate Group Marks
    GroupMarks = CalculateGroupMarks.Function(PopList, AssignedGroups)
    print("\nGroup Marks")
    PrintFormattedList(GroupMarks)

    # MODEL
    CalcResultArray = []
    if Model == "RA1":
        CalcResultArray = ReflectiveAccounts1(PopList, GroupMarks, AssignedGroups, GroupSize)
    elif Model == "RA2":
        CalcResultArray = ReflectiveAccounts2(PopList, GroupMarks, AssignedGroups, GroupSize)
    elif Model == "IPA":
        CalcResultArray = InverseProblemApproach(GroupMarks, AssignedGroups, n, GroupSize)
    elif Model == "PA1":
        CalcResultArray = PeerAssessment1(PopList, GroupMarks, AssignedGroups, GroupSize)
    elif Model == "PA2":
        CalcResultArray = PeerAssessment2(PopList, GroupSize, GroupMarks, AssignedGroups)
    elif Model == "SOPP":
        CalcResultArray = SelfOrganisedPeerPressure(GroupMarks, AssignedGroups, n)
    else:
        print("There is no program for this model")
        return

    print("\nModel Results")
    PrintFormattedList(CalcResultArray)
    print("Maximum individual mark is:", '%.1f' %max(CalcResultArray))

    # Analysis
    Results = Analysis.ResultArray(PopList, CalcResultArray)
    print("\nAnalysis")
    PrintResults(Results)
  
    return [PopList, CalcResultArray]

def RunAllModels(n,GroupSize):
    # Create the population
    PopList = Population.Function(n)
    # Assign the groups
    AssignedGroups = AssignGroup.Function(n,GroupSize)
    #Calculate Group Marks
    GroupMarks = CalculateGroupMarks.Function(PopList, AssignedGroups)
    # RA1 MODEL
    CalcResultArray = ReflectiveAccounts1(PopList, GroupMarks, AssignedGroups, GroupSize)
    RA1Results = Analysis.ResultArray(PopList, CalcResultArray)
    # RA2 MODEL
    CalcResultArray = ReflectiveAccounts2(PopList, GroupMarks, AssignedGroups, GroupSize)
    RA2Results = Analysis.ResultArray(PopList, CalcResultArray)
    # IPA MODEL
    CalcResultArray = InverseProblemApproach(GroupMarks, AssignedGroups, n, GroupSize)
    IPAResults = Analysis.ResultArray(PopList, CalcResultArray)
    # PA1 MODEL
    CalcResultArray = PeerAssessment1(PopList, GroupMarks, AssignedGroups, GroupSize)
    PA1Results = Analysis.ResultArray(PopList, CalcResultArray)
    # PA2 MODEL
##    CalcResultArray = PeerAssessment2(PopList, GroupMarks, AssignedGroups)
##    PA2Results = Analysis.ResultArray(PopList, CalcResultArray)
    # SOPP MODEL
    CalcResultArray = SelfOrganisedPeerPressure(GroupMarks, AssignedGroups, n)
    SOPPResults = Analysis.ResultArray(PopList, CalcResultArray)
    #Create List of Results
    Results = [RA1Results, RA2Results, [], PA1Results, [], SOPPResults]
    for result in Results:
        print("\nAnalysis")
        PrintResults(result)

Perfect = [[0,100],[0,100]]
P_List = SingleModelWithPrint(52,4,"SOPP")
    
##for n in range(0,1):
##    TempResults = SingleModelWithPrint(20,4,"RA2")
##    P_List.append(TempResults)

    
    
#RunAllModels(20,4)



#P_List = [[1,2,3], [1,2,3]]

plt.plot(P_List[0], P_List[1], label='Model Results', marker='x', linestyle='')
plt.plot(Perfect[0], Perfect[1], label='Ideal Results', marker='', linestyle='-')


plt.legend(loc='lower right')

plt.title("Inverse Problem Approach model")
plt.xlabel('Ideal mark')
plt.ylabel('Actual mark allocated')

plt.xlim(0,100)
plt.ylim(0,100)

plt.show()
