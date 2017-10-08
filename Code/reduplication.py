import csv

words = []
with open('/Users/annariehle/Desktop/Coding Projects/GA Data Science/ds-dc-21/projects/words.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		words.append(''.join(row))

def Single_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 1 and len(word) - 1 > 0:
			if word[i:i+1] == word[i+1:i+2]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 1:
			print 0
		elif len(word) - 1 <= 0:
			print 0	

def Double_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 3 and len(word) - 3 > 0:
			if word[i:i+2] == word[i+2:i+4]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 3:
			print 0
		elif len(word) - 3 <= 0:
			print 0	

def Triple_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 5 and len(word) - 5 > 0:
			if word[i:i+3] == word[i+3:i+6]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 5:
			print 0
		elif len(word) - 5 <= 0:
			print 0		

def Quad_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 7 and len(word) - 7 > 0:
			if word[i:i+4] == word[i+4:i+8]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 7:
			print 0
		elif len(word) - 7 <= 0:
			print 0		

def Quin_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 9 and len(word) - 9 > 0:
			if word[i:i+5] == word[i+5:i+10]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 9:
			print 0
		elif len(word) - 9 <= 0:
			print 0		

def Hex_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 11 and len(word) - 11 > 0:
			if word[i:i+6] == word[i+6:i+12]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 11:
			print 0
		elif len(word) - 11 <= 0:
			print 0	

def Sept_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 13 and len(word) - 13 > 0:
			if word[i:i+7] == word[i+7:i+14]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 13:
			print 0
		elif len(word) - 13 <= 0:
			print 0		

def Oct_Redup(words):
	for word in words:
		print word, 
		i = 0
		while i < len(word) - 15 and len(word) - 15 > 0:
			if word[i:i+8] == word[i+8:i+16]:
				print 1
				break
			else:
				i += 1
		if i == len(word) - 15:
			print 0
		elif len(word) - 15 <= 0:
			print 0	

Single_Redup(words)