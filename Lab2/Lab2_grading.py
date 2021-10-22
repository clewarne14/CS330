"""
 Grading code for Lab 2

 Written by Instructor: Dr. Cao
 Date: the day you read this script

 Instructions: This code is written by Dr. Cao for your reference. You may or may not use it, if you don't, your lab 2 grade could be a mystery :)

"""
import os
import math
import random
try:
    from Lab2_solution import train,train2,NBtest,scanAttributes,trainFlex,trainFlex2,NBFlextest,EvaNB
except:
    #print(e)
    try:
        from Lab2 import train,train2,NBtest,scanAttributes,trainFlex,trainFlex2,NBFlextest,EvaNB
    except:
        print("Error, please rename your lab submission to Lab1.py, and please also make sure you have implemented all methods: printInorder,printPostorder,printIndented,ExtractTokenFromString,getToken,getNumber,getProduct,getProduct2,getSum,getNumber2,SaveTokenToFile, LoadTokenToFile")
        sys.exit(0)

def generateTraining(output,numFeature = None, FeatureValues = None, numRecord = None):
    """
    This function will randomly generate the training data
    """
    random.seed = 330
    if numFeature == None:
        numFeature = random.randrange(3,20)
    if FeatureValues == None:
        FeatureValues = random.randrange(0,100)
    if numRecord == None:
        numRecord = random.randrange(100,5000)
    # get the header
    fh = open(output,"w")
    fh.write("#output")
    for i in range(numFeature):
        fh.write("|attr"+str(i))
    fh.write("\n")
    # save each training record
    for r in range(numRecord):
        rOut = random.randrange(2)
        fh.write(str(rOut))
        for i in range(numFeature):
            rValue = random.randrange(FeatureValues)
            fh.write(" "+str(rValue))
        fh.write("\n")
    fh.close()

    return(numFeature,FeatureValues,numRecord)

def generateTest(numFeatureRange, featureValuesRange, output):
    """
    This function will generate random testing data without label
    """
    numRecord = random.randrange(100,5000)
    fh = open(output,"w")
    for r in range(numRecord):
        fh.write("-1")
        for i in range(numFeatureRange):
            rValue = random.randrange(featureValuesRange)
            fh.write(" "+str(rValue))
        fh.write("\n")
    fh.close()
    return numRecord
def deleteTemFile(tobeDeleted):
    if os.path.isfile(tobeDeleted):
        os.system("rm "+tobeDeleted)

def verify(input, totalAmount):
    """
    Simply check if the total amount matches
    """
    with open(input,"r") as fh:
        for line in fh:
            if line.strip() == "":
                continue
            totalAmount-=1
    return totalAmount == 0


finalScore = 0

print("Preparing environment and start testing ...")
# normal and easy test
TrainingData = "CAOTRAINING_testTraining.txt"
TestingData = "CAOTEST_testNoLabel.txt"
ModelPath = "CAOMODEL.txt"
PredictionData = "CAOPREDICTION_testPred.txt"
deleteTemFile(TrainingData)
deleteTemFile(TestingData)
deleteTemFile(ModelPath)
deleteTemFile(PredictionData)
(N,F,NRecord) = generateTraining(TrainingData,numFeature=10,FeatureValues=10, numRecord=20)
NRecord = generateTest(N,F,TestingData)

try:
    train2(TrainingData,ModelPath)
except:
    print("error when calling train2 function")
try:
    NBtest(TestingData,ModelPath,PredictionData)
    if verify(PredictionData,NRecord):
        print("Great! Your train2 function seems working ...")
        finalScore+=3
    else:
        print("It seems your prediction didn't match with the total number of input? please check")
except:
    print("Error when calling NBtest or no prediction is made from your train2 function")


# now do more tests
deleteTemFile(TrainingData)
deleteTemFile(TestingData)
deleteTemFile(ModelPath)
deleteTemFile(PredictionData)

# now test trainFlex2 and NBFlextest
print("Now testing NBFlextest and trainFlex2, testing 1 ....")

(N,F,NRecord) = generateTraining(TrainingData,numFeature=20,FeatureValues=100, numRecord=20)
NRecord = generateTest(N,F,TestingData)

try:
    trainFlex2(TrainingData,ModelPath)
except:
    print("error when calling trainFlex2 function")

NBFlextest(TestingData,ModelPath,PredictionData)
if verify(PredictionData,NRecord):
    print("Great! Your trainFlex2 and NBFlextest function seems working on a simple test")
    finalScore+=3
else:
    print("It seems your prediction didn't match with the total number of input? please check trainFlex2 and NBFlextest")

print("Error when calling NBtest or no prediction is made by your trainFlex2 function")

# now test trainFlex2 and NBFlextest
print("Now testing NBFlextest and trainFlex2, testing 2 ....")
deleteTemFile(TrainingData)
deleteTemFile(TestingData)
deleteTemFile(ModelPath)
deleteTemFile(PredictionData)
(N,F,NRecord) = generateTraining(TrainingData)
NRecord = generateTest(N,F,TestingData)

try:
    trainFlex2(TrainingData,ModelPath)
except:
    print("error when calling trainFlex2 function")
try:
    NBFlextest(TestingData,ModelPath,PredictionData)
    if verify(PredictionData,NRecord):
        print("Great! Your trainFlex2 and NBFlextest function seems working on a difficult task")
        finalScore+=4
    else:
        print("It seems your prediction didn't match with the total number of input? please check trainFlex2 and NBFlextest")
except:
    print("Error when calling NBtest or no prediction is made by your trainFlex2")

# now test trainFlex2 and NBFlextest
print("Now testing NBFlextest and trainFlex2, testing 3 ....")
deleteTemFile(TrainingData)
deleteTemFile(TestingData)
deleteTemFile(ModelPath)
deleteTemFile(PredictionData)
(N,F,NRecord) = generateTraining(TrainingData)
NRecord = generateTest(N,F,TestingData)

try:
    trainFlex2(TrainingData,ModelPath)
except:
    print("error when calling trainFlex2 function")
try:
    NBFlextest(TestingData,ModelPath,PredictionData)
    if verify(PredictionData,NRecord):
        print("Great! Your trainFlex2 and NBFlextest function seems working on a difficult task again")
        finalScore+=4
    else:
        print("It seems your prediction didn't match with the total number of input? please check trainFlex2 and NBFlextest")
except:
    print("Error when calling NBtest or no prediction is made from trainFlex2")


print("Your total score is " + str(finalScore))
print("The max you can get here is 14. You should get anther 2 points when you post your comment on discord, and another 4 points once you also show the performance of weka and your model on the provided training dataset")
deleteTemFile(TrainingData)
deleteTemFile(TestingData)
deleteTemFile(ModelPath)
deleteTemFile(PredictionData)
