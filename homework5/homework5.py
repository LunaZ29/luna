#!/usr/bin/env python3
#2.1 VOCAB REVIEW
# 1. git vs github: git is the version control tool that runs on your computer, github is the website that hosts your git repos online
# 2. terminal vs command line: the terminal is the app/window you type in, the command line is the actual text interface where you type commands
# 3. local vs remote repository: local is the copy of the repo on your computer, remote is the copy stored online (like on github)
# 4. version control: a system that tracks changes to your files over time so you can go back to older versions and work with other people
# 5. staging area: where changes go after git add, it holds what will be included in the next commit
# 6. git add: adds changes to the staging area
# 7. git commit: saves the staged changes as a snapshot in your local repo with a message
# 8. git push: sends your local commits up to the remote repo
# 9. git status: shows which files are changed, staged, or untracked
# 10. git pull: grabs the newest changes from the remote repo and merges them into your local one
# 11. pwd: print working directory, shows the folder you are in right now
# 12. ls: lists the files and folders in your current directory
# 13. cd: change directory, moves you into a different folder
# 14. nano: opens a simple text editor in the terminal
# 15. touch: makes a new empty file
# 16. mv: moves a file to a new place or renames it
# 17. rm: deletes a file
# 18. cat: prints the contents of a file in the terminal

#2.2 A DIRECTORY TREE
# 1. pwd
# 2. ls
# 3. cd ../brianna_repo
#    git pull
# 4. mv homework.py ../judy_decal/homework/
# 5. cd ../judy_decal/homework
# 6. cat homework.py
# 7. git add .
#    git commit -m "done with homework"
#    git push origin main
# 8. the error means the remote repo has changes that judy doesnt have on her computer,
#    she tried to push without pulling the newest changes first. to fix it:
#    git pull origin main
#    git push origin main
# 9. cd ~/Recent/

#3.1 DATA TYPES
def checkDataType(x):
    return type(x).__name__

#3.2 CONDITIONALS
def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#4 LOOPS
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#5.1 LISTS
def duplicateList(list):
    newlist = []
    for item in list:
        newlist.append(item)
        newlist.append(item)
    return newlist

#5.2 DEBUGGING
# it was missing the colon after def square(num)
def square(num):
    return num * num

#6.2 FAVORITE FUNCTION
print(duplicateList(["a", "b", "c"]))
