#!/usr/bin/env python3
import subprocess
import sys
import os
import string

# sort ignore the case
# def sortFunction(x):
#    x = x.lower()
#    for index in range(len(x)):
#        if x[index] in string.ascii_lowercase or x[index] in string.digits:
#            return x[index:]


def dfsTree(curPath, prefix):
    files = []
    for fileName in os.listdir(curPath):
        if fileName[0] != '.':
            files.append(fileName)
    # sort all the files
    files.sort()
    # print (files)
    dirCount = 0
    fileCount = 0
    for index in range(len(files)):
        fileName = files[index]
        if index < len(files) - 1:
            curPrefix = "├── "
            subdirPrefix = "│   "
        else:
            curPrefix = "└── "
            subdirPrefix = "    "
        print(prefix + curPrefix + fileName)
        if os.path.isfile(os.path.join(curPath, fileName)):
            fileCount += 1
        else:
            dirCount += 1
            # recursively call dfsTree
            tempDirCount, tempFileCount = dfsTree(os.path.join(curPath, fileName), prefix + subdirPrefix)
            dirCount += tempDirCount
            fileCount += tempFileCount
    return dirCount, fileCount


def tree(path):
    print(path)
    dirCount, fileCount = dfsTree(path, "")
    print()
    if dirCount != 1:
        dirString = " directories, "
    else:
        dirString = " directory, "
    if fileCount != 1:
        fileString = " files"
    else:
        fileString = " file"
    print(str(dirCount) + dirString + str(fileCount) + fileString)


if __name__ == '__main__':
    if (len(sys.argv) > 2):
        print("Invalid.")
        sys.exit()
    path = "."
    if len(sys.argv) == 2:
        path = sys.argv[1]
    tree(path)
