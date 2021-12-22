#!/usr/bin/env python

file = open("books.txt", "r")

titles = file.readlines()

alist = []
x = 0
code = ""
length = 0
letter =""

for title in titles:
    alist.append(title.rstrip('\n'))
    length = len(alist[x])
    letter = alist[x][0] 
    code = letter + str(length)
    x += 1
    print (code) 

file.close()

