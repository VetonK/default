# -*- coding: utf-8 -*-
#!/usr/bin/env python

# USACH - nov 2012 - c.durr
# depth first search for the n-queen problem
# with forward check and arc-consistancy

import sys

n = int(sys.argv[1])

# the n-queen instance

Vars = range(n)
Vals = range(n)

# the actual constraint: is assigning queen x to u and queen y to v not conflicting?
def isValid(x,u, y,v):
    return u!=v and u+x-y!=v and u-x+y!=v

# domain of variables. Read only the first size[x] values, the rest are deleted values
dom = [[u for u in Vals] for x in Vals]
size = [n for x in Vals]

# loop over domain of x
def domain(x):
    for i in range(size[x]):
        yield dom[x][i]

# context history
hst = []
def saveContext():
    global size, hst
    hst.append(size[:])

def restoreContext():
    global size, hst
    size = hst.pop()

# remove i-th value of domain of x
def removeVal(x,i):
    global size
    size[x]-=1
    dom[x][i], dom[x][size[x]] = dom[x][size[x]], dom[x][i]

# returns set of variables which domain got reduced
def forwardCheck(x):
    Q = set()
    u = val[x]
    for y in Vars:
        if y!=x and val[y]==None:
            i=0
            while i<size[y]:
                v = dom[y][i]
                if not isValid(x,u, y,v):
                    removeVal(y,i)
                    Q.add(y)
                else:
                    i += 1
    return Q

# make arc-consistant
def AC3(Q):
    while Q:
        y = Q.pop()
        for x in Vars:
            if x!=y and val[x]==None and revise(x,y):
                Q.add(x)

# make the arc (x,y) consistant
def revise(x,y):
    i=0
    hasChanged = False
    while i<size[x]:
        u = dom[x][i]
        if not hasSupport(x,u,y):
            removeVal(x,i)
            hasChanged = True
        else:
            i+=1
    return hasChanged

def hasSupport(x,u, y):
    for v in domain(y):
        if isValid(x,u, y,v):
            return True
    return False
            
# the variables

val = [None for x in Vars]

def isSolved():
    for x in Vars:
        if val[x]==None:
            return False
    return True

# select most constrained variable
def selectVar():
    F = [(size[x],x) for x in Vars if val[x]==None]
    return min(F)[1]

nbNodes = 0
def solve():
    global nbNodes
    nbNodes += 1
    if isSolved():
        return True
    x = selectVar()
    for u in domain(x):
        val[x] = u
        saveContext()
        AC3(forwardCheck(x))
        if solve():
            return True
        restoreContext()
        val[x] = None
    return False

# is not necessary anymore with the forward check
def isConsistant(x,u):
    for y in Vars:
        if x!=y and val[y]!=None:
            if not isValid(x,u, y,val[y]):
                return False
    return True

#main program
AC3(set(Vars))
solve()
print (val)
print (nbNodes)
