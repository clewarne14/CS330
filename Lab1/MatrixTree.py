"""
 Name: Charlie LeWarne
 Assignment: Lab 1
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: September 25, 2021
 Sources consulted: https://note.nkmk.me/en/python-check-int-float/, to check if an object is integer or a float

 Known Bugs: None

 Creativity: None

 Instructions: Actually the Lab1 could be extended to handle nested list (like matrix) values. This assignment is designed to extend your lab1,
 Run the grading program, get result; currently the grading program gives me 10/10 points

"""
import sys
import pickle

class MatrixTree:
    """MatrixTree class. The node in the tree would be nested list to represent a matrix"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)


def dim(a):
    """
    Reference function to check the dimension of your tree node
    """
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])

def sum_two_nodes(node1, node2):
    """
    This method will calculate the sum of two nodes (two dimensional matrix) in the tree, and return the result as nested list. Return None when there is an issue to calculate the result, like dimension didn't match, not 2 dimension, etc.
    Example:
         sum_two_nodes([[10.0,10],[20,20]], [[20,20],[20,20]]) will return [[30.0,30.0],[40.0,40.0]]
         sum_two_nodes([[20,20]], [[20,20],[20,20]]) will return None
         sum_two_nodes([[20,20]], '+') will return None
    """
    result = []
    resultTemp = []
    i=0
    j=0
    # write your code
    #print("Output", len(node1[0]))
    #print("Test", dim(node1))
    if len(node1) != len(node2):
        return None
    while i < len(node1):
        while j < len(node1[0]):
            if (not isinstance(node1[i][j], int) and not isinstance(node1[i][j], float)) or (not isinstance(node1[i][j], int) and not isinstance(node1[i][j], float)):
                return None
            resultTemp.append(node1[i][j] + node2[i][j])
            j=j+1
        result.append(resultTemp)
        resultTemp = []
        i=i+1
        j=0
    return result

def totalValueMatrix(tree):
    """
    recursively count the total values in the matrix tree.
    For example, a tree myTree= MatrixTree('+', MatrixTree([[1,2],[1,2]]), MatrixTree('+', MatrixTree([[2,3],[3,5]]), MatrixTree([[0,0],[0,0]])))
          totalValueMatrix(myTree) would return: [ [3.0, 5.0], [4.0, 7.0]]
    return None if anything is wrong
    To make things simple, we only consider '+' here
    """
    # write your code
    totalOut=0
    output=[]
    outputTemp=[]
    i=0
    j=0
    
    if tree.value=='+':
        return sum_two_nodes(totalValueMatrix(tree.left), totalValueMatrix(tree.right))
    else:
        return tree.value
        # while i < len(tree.value):
        #     while j < len(tree.value[i]):
        #         if (not isinstance(tree.value[i][j], int) and not isinstance(tree.value[i][j], float)) or (not isinstance(tree.value[i][j], int) and not isinstance(tree.value[i][j], float)):
        #             return None
        #         totalOut=totalOut+tree.value[i][j]
        #         j=j+1
        #     i=i+1
        #     j=0
    return totalOut
    pass

def main():
    # testing your code here
    print("expected: [ [3.0, 5.0], [4.0, 7.0]]")
    print(sum_two_nodes([[10,10],[20,20]], [[20,20],[20,20]]))
    print("expected: None")
    print(sum_two_nodes([[10,10],['a',20]], [[20,20],[20,20]]))
    print("expected: None")
    print(sum_two_nodes([[20,20]], [[20,20],[20,20]]))
    print("expected: [ [3.0, 5.0], [4.0, 7.0]]")
    myTree= MatrixTree('+', MatrixTree([[1,2],[1,2]]), MatrixTree('+', MatrixTree([[2,3],[3,5]]), MatrixTree([[0,0],[0,0]])))
    print(totalValueMatrix(myTree))
    print()

if __name__ == "__main__":
    main()
