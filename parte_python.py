# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:50:58 2021

@author: sti_2
"""
#! /usr/bin/python
import os
import time

arquivo = open("pid.txt", "w")
pid1 = os.getpid()
arquivo.write(str(pid1))
arquivo.close()
for x in range(0, 3):
	print('2: I am alive')
	time.sleep(.5)
arquivo = open("pid.txt", "w")
arquivo.write(str(0))
arquivo.close()
print('2: I gonna die now, bye')

'''
o script abre o arquivo pid.txt(ou cria caso não exista ) e
escreve seu pid de funcionamento , depois fica vivo por 1.5 seg
em seguida escreve uma string 0 quando não esta mais em operação
'''



