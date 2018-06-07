# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:36:29 2018

@author: Veton
"""

#
import sys
nbr=5
cube=[[' ',' ','+','-','-','-','+'],[' ','/',' ',' ',' ','/','|'],['+','-','-','-','+',' ','|'],['|',' ',' ', ' ','|',' ','+'],['|',' ',' ',' ','|','/'],['+','-','-','-','+',]]
 
#liste =[]
def imprime_cube(cube):
    i=j=0
    while(j<len(cube)):
        i=0
        while(i<len(cube[j])):
            print(cube[j][i],end='')
            i=i+1

        print()
        j=j+1
    return


def imprime_multi_cube():
    print('hello')
    
imprime_multi_cube()

