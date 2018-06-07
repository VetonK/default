# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:36:29 2018

@author: Veton
"""

#
import sys

nbr=5
cube=[['+','-','-','-','+'],['/',' ',' ',' ','/','|'],['+','-','-','-','+',' ','|'],['|',' ',' ', ' ','|',' ','+'],['|',' ',' ',' ','|','/'],['+','-','-','-','+',]]
surface= [['#'] * 20]*20

def imprime_cube(surface):
  for j in range(len(surface)):
            for i in range(len(surface[j])):
                print(surface[j][i],end='')
            print('')
  return


def ajoute_cube(z):
    for x in range(z):
        for j in range(len(cube)):
            for i in range(len(cube[j])):
                print(cube[j][i],end='')
                surface[j][i]=cube[j][i]
            print()
    return
def imprime_multi_cube():
    return


imprime_cube(surface)
print('hello')
print(cube)
ajoute_cube(1)
print(surface)
imprime_cube(surface)

#imprime_multi_cube()

