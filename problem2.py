import numpy as np

dValue = 1.0
print("Setting the value of D as:", dValue)
lValue = 1.2
print("Setting the value of L as:", lValue)
numOfSamples = 500
print("Setting the number of Samples as:", numOfSamples)
observationList=[]

def main():
    observationList = np.zeros(numOfSamples)
    for i in range(numOfSamples):
        observationList[i] = didTheNeedleDrop(dValue, lValue)
    expectedValue = getExpectedValue(dValue, lValue)
    calculatedValue = getCalculatedValue(observationList)
    pValue = expectedValue - calculatedValue   
    return pValue

def didTheNeedleDrop(dValue, lValue):
    thetaValue = np.random.uniform(0, np.pi/2)
    return True if np.random.uniform(0,dValue/2) < lValue/2*np.sin(thetaValue) else False
 
def getCalculatedValue(observationList):
    calculatedValue = np.average(observationList)
    print("Calulated Value Is: ", calculatedValue)
    return calculatedValue

def getExpectedValue(dValue, lValue):
    if lValue<dValue:
        expectedValue=2*lValue/np.pi*dValue   
    else:
        expectedValue=(2/np.pi)*(-(np.sqrt(((lValue/dValue)**2)-1))+(lValue/dValue)+(np.arccos(dValue/lValue)))
    print("Expected Value Is: ", expectedValue)
    return expectedValue

if __name__ == '__main__':
    print("P Value: ", main())