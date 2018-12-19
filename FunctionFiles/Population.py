import random

def Function(n):

    PopulationArray = []
    
    for x in range(0, n):
        
        PopulationArray.append(int(random.gauss(60, 10)))

        if PopulationArray[x] > 100:
            PopulationArray[x] = 100

        elif PopulationArray[x] < 0:
            PopulationArray[x] = 0

    
    return PopulationArray
