"""
 Grading code for MatrixTree

 Written by Instructor: Dr. Cao
 Date: the day you read this script

 Instructions: This code is written by Dr. Cao for your reference. You may or may not use it, if you don't, your lab 1 grade could be a mystery :)

"""
import sys
try:
    from MatrixTree_solution import dim,sum_two_nodes,totalValueMatrix
except:
    #print(e)
    try:
        from MatrixTree import dim,sum_two_nodes,totalValueMatrix
    except e:
        print(e)
        print("Error, please rename your lab submission to MatrixTree.py, and please also make sure you have implemented all methods: dim,sum_two_nodes,totalValueMatrix")
        sys.exit(0)

class MatrixTree:
    """Tree class. This is used for expression trees"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)


def main():
    totalScore = 0
    print(sum_two_nodes([[10,10],[20,20]], [[20,20],[20,20]]))
    # now test sum_two_nodes, 6 points
    totalScore+=sum( 2 *
    [sum_two_nodes([[10,10],[20,20]], [[20,20],[20,20]]) == [[30.0, 30.0], [40.0, 40.0]],
    sum_two_nodes([[10,10],['a',20]], [[20,20],[20,20]]) == None,
    sum_two_nodes([[21,21]], [[20,20],[20,20]]) == None]
    )
    
    # now test totalValueMatrix, 4 points
    totalScore+=sum([
    [[3.0, 5.0], [4.0, 7.0]] == totalValueMatrix(MatrixTree('+', MatrixTree([[1,2],[1,2]]), MatrixTree('+', MatrixTree([[2,3],[3,5]]), MatrixTree([[0,0],[0,0]])))),
    [[3.0, 459.0, 36.0, -96.0], [4.0, 8.0, 114.0, 907.0]] == totalValueMatrix(MatrixTree('+', MatrixTree([[1,2,3,4],[1,2,53,63]]), MatrixTree('+', MatrixTree([[2,3,31,-100],[3,5,56,832]]), MatrixTree([[0,454,2,0],[0,1,5,12]])))),
    [[4.0, 9.0, 41.0, -95.0], [4.0, 461.0, 111.0, 895.0], [2.0, 9.0, 19.0, 14.0]] == totalValueMatrix(MatrixTree('+', MatrixTree([[1,2,3,4],[1,2,53,63],[1,4,7,1]]), MatrixTree('+', MatrixTree([[2,3,31,-100],[3,5,56,832],[1,4,7,1]]), MatrixTree([[1,4,7,1],[0,454,2,0],[0,1,5,12]])))),
    None == totalValueMatrix(MatrixTree('+', MatrixTree([[1,2,3,4],[1,2,5,7],[1,2,53,63],[1,4,7,1]]), MatrixTree('+', MatrixTree([[2,3,31,-100],[3,5,56,832],[1,4,7,1]]), MatrixTree([[1,4,7,1],[0,454,2,0],[0,1,5,12]]))))
    ]
    )
    print("Your total score is (max 10):")
    print(totalScore)

if __name__ == "__main__":
    main()
