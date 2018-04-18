#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:16:42 2018

@author: divyanshu
"""

#%%

with open('hi', 'r') as myfile:
		   data=myfile.read().replace('\n', '')
	
		 
	
count = 0
t = []
for i in data:
	
	if count != 100:
		count += 1
		if len(t) == 0:
			t = i
		else:
			t += i
	else:
		break
		
print(t)	 

"MA"
"MAIK"
"MAIKIG"
"MAIKIGIN"
"MAIKIGINGF"
"MAIKIGINGFGRIGRIVFRA"
