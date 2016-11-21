#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ali Abdulmadzhidov
# 21.11.2016 22:39
# InnoCTF Eatable

from pwn import *
from pprintpp import pprint as pp

file = open("dict", "a+")

# for i in xrange(500):
	
r = remote("188.130.155.58" ,10000)
temp = ""

def checkuniq(word, lines):
	for item in lines:
		if item[:-1] == word:
			return True
	return False
 

for i in xrange(501):
	word = r.recv()
	print i, word
	if word == "FAIL. TRY AGAIN":
		file.write(temp+"\n")
		file.close()
		print "OK"
	file.seek(0,0)
	if not checkuniq(word,file.readlines()):
		r.send("несъедобное")
	else:
		r.send("съедобное")
	temp = word
r.interactive()



