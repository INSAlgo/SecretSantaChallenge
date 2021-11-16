import time
from os import listdir

# You are free to add/modify as many things as you like in this template

"""
You can use these global variable to check for time limit
To use them in a function, write:

global timeLimitCheck           # tell python that you gonna use (change the value) the global variable
timeLimitCheck = time.time()    # set the time at the beginning of your method (it is the start time)

and to check if the time limit is exceeded, write:

if time.time()-timeLimitCheck > TIME_LIMIT:
    # return your timeLimitOutput 
#Note : to just read a global variable, you don't need to write "global <nameOfVariable>"
"""

timeLimitCheck = time.time()
TIME_LIMIT = 2  # Time limit in seconds (you can change this if you want)

"""
Tests cases descriptions:
TestCase[number 1-10].txt are test cases made by hand some basic cases, some not

TestCase[N1]-[N2].txt are test cases randomly generated
N1 -> The percentage of chance that to nodes are linked
N2 -> The number of nodes

Note that the goal is not to pass every testCases, some of them are almost impossible, they are their to chalenge you !
"""
def inputReading(path: str):
    # Open the file
    file = open(path, 'r')

    # Put all lines into a array
    fileLines = file.readlines()
    for i in range(len(fileLines)):
        fileLines[i] = fileLines[i].strip('\n')

    # TODO 1: Write the parsing of the input file (hint: you can try to use a adjacency list)


def solution():
    # TODO 2: Write a solution here (You can creat more methods to try more things)
    return


def checkIfSolutionIsRight(solution) -> bool:
    # TODO 3: (Optional: it depends on your solution method) Check if a computed solution is correct
    return True


if __name__ == '__main__':
    for fileName in listdir("TestCases"):
        adjacency = inputReading("TestCases/" + fileName)
        print(fileName)
        start_time = time.time()
        print("Solution :", solution())
        print("\tTime = ", time.time() - start_time, '\n')
        print("--------------------------------------")
