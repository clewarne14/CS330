"""
 Name: Charlie LeWarne
 Assignment: Lab 2 - Naive Bayesian Model
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: October 1, 2021
 Sources consulted: Joshua Berkenpass, Chris Holland - For advice on finding bugs, deleting the try except statement from the
 grading file for testing(I changed it back to finish and submit), and suggesting using a .zip file to submit

 Known Bugs: None

 Creativity: None

 Instructions: Run with the different inputs and get a Performance.txt output

"""
import sys
import argparse
import math



def train(data, model):
    """
    This is the main function. It is going to read
    TrainingData.txt, and calculate all probablities, save them as a model file.
    You should design what kind of data format to save the model, and make sure
    you could read them back when you do the prediction.
    """
    totalcount = 0
    playcount = 0
    r,c = 10,2            # total rows and columns for each attribute table. In the example training dataset, each attribute could have 10 different values.
    outlook = [0] * r
    temp = [0] * r
    humidity = [0] * r
    wind = [0] * r
    """Method to read data from file and arrange in matrix"""
    for i in range(int(r)):
        outlook[i] = [0] * c
        temp[i] = [0] * c
        humidity[i] = [0] * c
        wind[i] = [0] * c
    with open(data) as file:
        file.readline()
        for line in file:
            current = [int(i) for i in line.split()]
            if(current.pop(0) == 0):
                totalcount +=1
                outlook[current.pop(0)-1][0] +=1
                temp[current.pop(0)-1][0] +=1
                humidity[current.pop(0)-1][0] += 1
                wind[current.pop(0)-1][0] += 1
            else:
                totalcount +=1
                playcount += 1
                outlook[current.pop(0)-1][1] += 1
                temp[current.pop(0)-1][1] += 1
                humidity[current.pop(0)-1][1] += 1
                wind[current.pop(0)-1][1] += 1
    """Method to calculate probabilities"""
    for i in range(r):
            outlook[i][0] = math.log(float(outlook[i][0])/(totalcount-playcount))
            temp[i][0] = math.log(float(temp[i][0])/(totalcount-playcount))
            humidity[i][0] = math.log(float(humidity[i][0])/(totalcount-playcount))
            wind[i][0] = math.log(float(wind[i][0])/(totalcount-playcount))
            outlook[i][1] = math.log(float(outlook[i][1])/(playcount))
            temp[i][1] = math.log(float(temp[i][1])/(playcount))
            humidity[i][1] = math.log(float(humidity[i][1])/(playcount))
            wind[i][1] = math.log(float(wind[i][1])/(playcount))

    """Method to write probabilities"""
    with open(model,"w") as f:
        f.write(str(totalcount) + '\n')
        f.write(str(playcount) + '\n')
        for i in range(r):
            for j in range(c):
                f.write(str(outlook[i][j] ) + ' ')
            f.write('\n')
        for i in range(r):
            for j in range(c):
                f.write(str(temp[i][j] ) + ' ')
            f.write('\n')
        for i in range(r):
            for j in range(c):
                f.write(str(humidity[i][j] ) + ' ')
            f.write('\n')
        for i in range(r):
            for j in range(c):
                f.write(str(wind[i][j] ) + ' ')
            f.write('\n')
        f.close()


def train2(data, model):
    """
    There is at least one bug in train function written by Dr. Cao, so it is not working on some input data like TrainingSpecialData.txt, implement train2 to fix that bug. Please be aware of any other potential bugs
    """
    # Write your code here
    """
    This is the main function. It is going to read
    TrainingData.txt, and calculate all probablities, save them as a model file.
    You should design what kind of data format to save the model, and make sure
    you could read them back when you do the prediction.
    """
    
    totalcount = 0
    playcount = 0
    r,c = 10,2            # total rows and columns for each attribute table. In the example training dataset, each attribute could have 10 different values.
    outlook = [0] * r
    temp = [0] * r
    humidity = [0] * r
    wind = [0] * r
    """Method to read data from file and arrange in matrix"""
    for i in range(int(r)):
        outlook[i] = [0] * c
        temp[i] = [0] * c
        humidity[i] = [0] * c
        wind[i] = [0] * c
    with open(data) as file:
        file.readline()
        for line in file:
            current = [int(i) for i in line.split()]
            if(current.pop(0) == 0):
                totalcount +=1
                outlook[current.pop(0)-1][0] +=1
                temp[current.pop(0)-1][0] +=1
                humidity[current.pop(0)-1][0] += 1
                wind[current.pop(0)-1][0] += 1
            else:
                totalcount +=1
                playcount += 1
                outlook[current.pop(0)-1][1] += 1
                temp[current.pop(0)-1][1] += 1
                humidity[current.pop(0)-1][1] += 1
                wind[current.pop(0)-1][1] += 1
    """Method to calculate probabilities"""
    playcount = playcount + 1
    for i in range(r):

            if outlook[i][0] == 0:
                outlook[i][0] = 0.5
            if temp[i][0] == 0:
                temp[i][0] = 0.5
            if humidity[i][0] == 0:
                humidity[i][0] = 0.5
            if wind[i][0] == 0:
                wind[i][0] = 0.5
            if outlook[i][1] == 0:
                outlook[i][1] = 0.5
            if temp[i][1] == 0:
                temp[i][1] = 0.5
            if humidity[i][1] == 0:
                humidity[i][1] = 0.5
            if wind[i][1] == 0:
                wind[i][1] = 0.5
            outlook[i][0] = math.log(float(outlook[i][0])/(totalcount-playcount))
            temp[i][0] = math.log(float(temp[i][0])/(totalcount-playcount))
            humidity[i][0] = math.log(float(humidity[i][0])/(totalcount-playcount))
            wind[i][0] = math.log(float(wind[i][0])/(totalcount-playcount))
            outlook[i][1] = math.log(float(outlook[i][1])/(playcount))
            temp[i][1] = math.log(float(temp[i][1])/(playcount))
            humidity[i][1] = math.log(float(humidity[i][1])/(playcount))
            wind[i][1] = math.log(float(wind[i][1])/(playcount))

    """Method to write probabilities"""
    with open(model,"w") as f:
        f.write(str(totalcount) + '\n')
        f.write(str(playcount) + '\n')
        for i in range(r):
            for j in range(c):
                f.write(str(outlook[i][j] ) + ' ')
            f.write('\n')
        for i in range(r):
            for j in range(c):
                f.write(str(temp[i][j] ) + ' ')
            f.write('\n')
        for i in range(r):
            for j in range(c):
                f.write(str(humidity[i][j] ) + ' ')
            f.write('\n')
        for i in range(r):
            for j in range(c):
                f.write(str(wind[i][j] ) + ' ')
            f.write('\n')
        f.close()
    pass

def NBtest(data, model, prediction):
    """
    This is the main function. It is load saved model file,
    and also load testing data TestDataNoLabel.txt, and apply the trained model to make predictions.
    You should save your predictions in prediction file, each line would be a label, such as:
    1
    0
    0
    1
    ...
    """
    """Method to load model"""
    totalcount,playcount,r,c = 0,0,10,2
    outlook = [0] * r
    temp = [0] * r
    humidity = [0] * r
    wind = [0] * r
    for i in range(int(r)):
        outlook[i] = [0] * c
        temp[i] = [0] * c
        humidity[i] = [0] * c
        wind[i] = [0] * c
    with open(model, 'r') as file:
        totalcount = file.readline()
        playcount = file.readline()

        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            outlook[i][0] = current.pop(0)
            outlook[i][1] = current.pop(0)
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            temp[i][0] = current.pop(0)
            temp[i][1] = current.pop(0)
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            humidity[i][0] = current.pop(0)
            humidity[i][1] = current.pop(0)
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            wind[i][0] = current.pop(0)
            wind[i][1] = current.pop(0)

    """Method to load data"""
    out_file = open(prediction,'w')
    with open(data,'r') as in_file:
        for line in in_file:
            current = [int(p) for p in line.split()]
            current1 = list(current)
            current.pop(0)

            yes = ((float(playcount)/float(totalcount)) *
            (outlook[current.pop(0)-1][1]) * (temp[current.pop(0)-1][1]) *
            (humidity[current.pop(0)-1][1]) * (wind[current.pop(0)-1][1]))

            no = ((float(playcount)/float(totalcount)) *
            (outlook[current1.pop(0)-1][0]) * (temp[current1.pop(0)-1][0]) *
            (humidity[current1.pop(0)-1][0]) * (wind[current1.pop(0)-1][0]))
            if yes > no:
                out_file.write("1\n")
            else:
                out_file.write("0\n")

def ARFFConvert(data, output):
    """
    This is the main function.
    Load the data from course website and convert it to ARFF format,
    so that Weka could accept them and load them. Check Weka Manual
    and examples of ARFF format.
    """
    with open(data,'r') as file1, open(output,'w') as file2:
        firstline = file1.readline().split('|')
        file2.write("@relation Play_Tennis \n\n")
        file2.write("@attribute " + firstline.pop(0).strip('#') + " {0,1}\n")
        file2.write("@attribute " + firstline.pop(0) + " {1,2,3,4,5,6,7,8,9,10}\n")
        file2.write("@attribute " + firstline.pop(0) + " {1,2,3,4,5,6,7,8,9,10}\n")
        file2.write("@attribute " + firstline.pop(0) + " {1,2,3,4,5,6,7,8,9,10}\n")
        file2.write("@attribute " + firstline.pop(0).strip() + " {1,2,3,4,5,6,7,8,9,10}\n\n")
        file2.write("@data\n")
        for line in file1:
            otherlines = [str(i) for i in line.split()]
            file2.write(otherlines.pop(0) + ",")
            file2.write(otherlines.pop(0) + ",")
            file2.write(otherlines.pop(0) + ",")
            file2.write(otherlines.pop(0) + ",")
            file2.write(otherlines.pop(0) + "\n")

def scanAttributes(data):
    """ Preprocesses the file to detect number of attributes and the amount of values for each attribute """
    num_attributes = 0
    num_values = []
    with open(data) as file:
        num_attributes = len(file.readline().split("|"))
        values = [set() for i in range(num_attributes)] # storing all unique values for each attribute

        # Grab all possible values for each attribute
        for line in file:
            current = [int(i) for i in line.split()]
            for i in range(len(current)):
                values[i].add(current[i])

        # Add an extra value for sets with 0 to fix issues that occur with the code below
        for i in values:
            if 0 in i: i.add(max(i)+1) # adds a new max that's 1 greater than the previous

        # Generate a list of total amount of values for each attribute
        total_rows = [max(values[i]) for i in range(num_attributes)]
        return total_rows.pop(0), total_rows # first value will be the number of columns


def trainFlex(data, model):
    """
    The train or train2 function could be improved by handling various number of features and feature values. Here is the reference code that will
    process the input data and get the total number of features, and then train the NB model on the training dataset. However, this code is still not perfect, please check it carefully and implement trainFlex2
    """
    totalcount = 0
    playcount = 0
    c,r = scanAttributes(data)            # total rows and columns for each attribute table. In the example training dataset, each attribute could have 10 different values.
    attributes = [ [0]*rows for rows in r]

    """Method to read data from file and arrange in matrix"""
    for attr in attributes:
        for i in range(len(attr)): # for each row in that attribute
            attr[i] = [0] * c

    with open(data) as file:
        file.readline()
        for line in file:
            current = [int(i) for i in line.split()]
            if(current.pop(0) == 0):
                totalcount +=1
                for attr in attributes:
                    attr[current.pop(0)-1][0] += 1
            else:
                totalcount +=1
                playcount += 1
                for attr in attributes:
                    attr[current.pop(0)-1][1] += 1

    """Method to calculate probabilities"""
    # if totalcount == playcount or playcount == 0:
    for attr in attributes:
        for i in range(len(attr)): # number of rows per attribute
            attr[i][0] = math.log(float(attr[i][0])/(totalcount-playcount))
            attr[i][1] = math.log(float(attr[i][1])/(playcount))

    """Method to write probabilities"""
    with open(model,"w") as f:
        f.write(str(totalcount) + '\n')
        f.write(str(playcount) + '\n')
        for attr in attributes:
            for i in range(len(attr)): # for each row in the attribute
                for j in range(c): # for each column
                    f.write(str(attr[i][j]) + ' ')
                f.write('\n')

        f.close()

def trainFlex2(data, model):
    """
    Sometimes trainFlex crashes similar to the one you have seen in train function, please implement trainFlex2 to fix that bug.
    """
    # write your code here
    totalcount = 0
    playcount = 0
    c,r = scanAttributes(data)            # total rows and columns for each attribute table. In the example training dataset, each attribute could have 10 different values.
    attributes = [ [0]*rows for rows in r]

    """Method to read data from file and arrange in matrix"""
    for attr in attributes:
        for i in range(len(attr)): # for each row in that attribute
            attr[i] = [0] * c

    with open(data) as file:
        file.readline()
        for line in file:
            current = [int(i) for i in line.split()]
            if(current.pop(0) == 0):
                totalcount +=1
                for attr in attributes:
                    attr[current.pop(0)-1][0] += 1
            else:
                totalcount +=1
                playcount += 1
                for attr in attributes:
                    attr[current.pop(0)-1][1] += 1

    """Method to calculate probabilities"""
    for attr in attributes:
        for i in range(len(attr)): # number of rows per attribute
            if float(attr[i][0]) == 0.0:
                attr[i][0] = 0.5
                totalcount = totalcount + 1
            if float(attr[i][1]) == 0.0:
                attr[i][1] = 0.5
                totalcount = totalcount + 1
            attr[i][0] = math.log(float(attr[i][0])/(totalcount-playcount))
            attr[i][1] = math.log(float(attr[i][1])/(playcount))

    """Method to write probabilities"""
    with open(model,"w") as f:
        f.write(str(totalcount) + '\n')
        f.write(str(playcount) + '\n')
        for attr in attributes:
            for i in range(len(attr)): # for each row in the attribute
                for j in range(c): # for each column
                    f.write(str(attr[i][j]) + ' ')
                f.write('\n')

        f.close()
    pass

def NBFlextest(data, model, prediction):
    """
    The NBtest function may not work well when you use trainFlex2 function to train your model, please update NBtest function so that it can handle the model generated from trainFlex2.
    You should feel free to store the model in the format that you prefer, as long as you are able to load it back correctly here :)
    """
    totalcount,playcount,r,c = 0,0,10,2
    outlook = [0] * r
    temp = [0] * r
    humidity = [0] * r
    wind = [0] * r
    for i in range(int(r)):
        outlook[i] = [0] * c
        temp[i] = [0] * c
        humidity[i] = [0] * c
        wind[i] = [0] * c
    with open(model, 'r') as file:
        totalcount = file.readline()
        playcount = file.readline()
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            outlook[i][0] = current.pop(0)
            outlook[i][1] = current.pop(0)
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            temp[i][0] = current.pop(0)
            temp[i][1] = current.pop(0)
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            humidity[i][0] = current.pop(0)
            humidity[i][1] = current.pop(0)
        for i in range(int(r)):
            line1 = file.readline()
            current = [math.exp(float(k)) for k in line1.split()]
            wind[i][0] = current.pop(0)
            wind[i][1] = current.pop(0)
    """Method to load data"""
    out_file = open(prediction,'w')
    with open(data,'r') as in_file:
        for line in in_file:
            current = [int(p) for p in line.split()]
            current1 = list(current)
            current.pop(0)

            # try:
            while len(outlook) <= current[0]-1:
                outlook.append([0,0])
            while len(temp) <= current[1]-1:
                temp.append([0,0])
            while len(humidity) <= current[2]-1:
                humidity.append([0,0])
            while len(wind) <= current[3]-1:
                wind.append([0,0])
            while len(outlook) <= current1[0]-1:
                outlook.append([0,0])
            while len(temp) <= current1[1]-1:
                temp.append([0,0])
            while len(humidity) <= current1[2]-1:
                humidity.append([0,0])
            while len(wind) <= current1[3]-1:
                wind.append([0,0])
            yes = ((float(playcount)/float(totalcount)) *
            (outlook[current.pop(0)-1][1]) * (temp[current.pop(0)-1][1]) *
            (humidity[current.pop(0)-1][1]) * (wind[current.pop(0)-1][1]))
            no = ((float(playcount)/float(totalcount)) *
            (outlook[current1.pop(0)-1][0]) * (temp[current1.pop(0)-1][0]) *
            (humidity[current1.pop(0)-1][0]) * (wind[current1.pop(0)-1][0]))
            if yes > no:
                out_file.write("1\n")
            else:
                out_file.write("0\n")

    pass

def EvaNB(predictionLabel, realLabel, output):
    """
    This is the main function. You should compare line by line,
     and calculate how many predictions are correct, how many predictions are not correct. The output could be:

    In total, there are ??? predictions. ??? are correct, and ??? are not correct.

    """
    correct,incorrect, length = 0,0,0
    with open(predictionLabel,'r') as file1, open(realLabel, 'r') as file2:
        pred = [line for line in file1]
        real = [line for line in file2]
        length = len(pred)
        for i in range(length):
            if pred.pop(0) == real.pop(0):
                correct += 1
            else:
                incorrect += 1
    Rate = correct/length

    result = "In total, there are "+str(length)+" predictions. "+str(correct)+" are correct and "+ str(incorrect) + " are incorrect. The percentage is "+str(Rate)
    with open(output, "w") as fh:
        fh.write(result)

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    if mode == "T":
        """
        The training mode
        """
        inputFile = options.input
        ARFFConvert(options.input,"TESTINGFILE.arff")
        outModel = options.output
        if inputFile == '' or outModel == '':
            showHelper()
        #train(inputFile,outModel)

        trainFlex2(inputFile, outModel)
    elif mode == "P":
        """
        The prediction mode
        """
        inputFile = options.input
        modelPath = options.modelPath
        outPrediction = options.output

        if inputFile == '' or modelPath == '' or outPrediction == '':
            showHelper()
        NBFlextest(inputFile,modelPath,outPrediction)
    elif mode == "E":
        """
        The evaluating mode
        """
        predictionLabel = options.input
        trueLabel = options.trueLabel
        outPerf = options.output
        if predictionLabel == '' or trueLabel == '' or outPerf == '':
            showHelper()
        EvaNB(predictionLabel,trueLabel, outPerf)
    pass

def showHelper():
    parser.print_help(sys.stderr)
    print("Please provide input augument. Here are examples:")
    print("python " + sys.argv[0] + " --mode T --input TrainingData.txt --output NBModel.txt")
    print("python " + sys.argv[0] + " --mode P --input TestDataNoLabel.txt --modelPath NBModel.txt --output TestDataLabelPrediction.txt")
    print("python " + sys.argv[0] + " --mode E --input TestDataLabelPrediction.txt --trueLabel LabelForTest.txt --output Performance.txt")

    print("python " + sys.argv[0] + " --mode T --input TrainingSpecialData.txt --output NBModel2.txt")
    sys.exit(0)


if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: T for training, and P for making predictions, and E for evaluating the machine learning model')
    parser.add_argument('--input', dest='input',
    default = '',    # default empty!
    help = 'The input file. For T mode, this is the training data, for P mode, this is the test data without label, for E mode, this is the predicted labels')
    parser.add_argument('--output', dest='output',
    default = '',    # default empty!
    help = 'The output file. For T mode, this is the model path, for P mode, this is the prediction result, for E mode, this is the final result of evaluation')
    parser.add_argument('--modelPath', dest='modelPath',
    default = '',    # default empty!
    help = 'The path of the machine learning model ')
    parser.add_argument('--trueLabel', dest='trueLabel',
    default = '',    # default empty!
    help = 'The path of the correct label ')
    if len(sys.argv)<3:
        showHelper()
    main()
