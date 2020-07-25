#!/bin/python3

import os
import nltk
from nltk import word_tokenize
import numpy as np
from numpy import linalg as la
import string
from nltk.corpus import stopwords

# I am attempting to design the program so that a single switch in "SETTINGS.py"
# will cause your classifier to use either the graphical or vectorized 
# approach without altering your actual Knn code


##################          Document Class            #######################	


# Parent
class Document:
	
## Instance Methods
# Call these like this: obj.func()

	# Initializer / Instance attributes
    def __init__(self, filename, stpwords = []):
		self.stopwords = stopwords.words('english') + stpwords
		self.doc_title = filename
		self.doc_raw_text = readFromFile(filename)        
		self.word_list = clean_text(self.doc_raw_text, self.stopwords)
		self.text_obj = nltk.Text(self.word_list)
		self.freq_dist = nltk.FreqDist(self.text_obj)
		
	def return_most_common(self):
		return self.freq_dist.most_common(50)


	def __str__(self):
		return "Title: {0}".format(self.doc_title)
	
## Static Methods
# Call these like this: comparison_tool.func()


	# This method takes in a filename, opens it, reads it, and returns its contents as a string
	# This method works on files that contain non-ascii characters, the original corpus
	# that Aaron has given us has non-ascii characters; this function strips those off
	# otherwise, these characters cause the default read() command to fail
	# uses OS library
	# Use this instead of python's read function
	
	# Function: DONE
	# Input: filename as string
	# Output [return value]: file contents as string
	def readFromFile(filename):
		f = os.open(filename, os.O_RDONLY)
		f_stats = os.fstat(f) # find size of the file
		text_in = os.read(f,s_stats.st_size) # read exactly that many bytes
		os.close(f)
		return str(text_in, 'utf-8', 'ignore') # convert from byte string to string
	
	# This function takes in file contents as a python string and cleans the text of stopwords
	# Needs updating
	# TODO
	def clean_text(raw_text, stopwords):
		raw_text = raw_text.lower()
		raw_text.replace('\'s','')
		text_list = word_tokenize(raw_text)
		text_list = [word for word in text_list if word.lower() not in stopwords and word not in string.punctuation]
		return text_list
		
		
##################          Vectorized Approach I           #######################	
		
		

# Child
class DocumentVectorized(Document):

## Instance Methods
# Call these like this: obj.func()	

	# Use this in KNN	
	def compareOperand(doc1, l2): # can be expanded to use bigrams and trigrams
		l1 = doc1.freq_dist.most_common(50) # extracted list of tuples
		return compute_cosine_similarity(l1,l2)
		
	def compare(doc1, doc2): # can be expanded to use bigrams and trigrams
		l1 = doc1.freq_dist.most_common(50) # extracted list of tuples
		l2 = doc2.freq_dist.most_common(50) # extracted list of tuples
		return compute_cosine_similarity(l1,l2)
		
		
## Static Methods
# Call these like this: comparison_tool.func()

	# TODO
	# This function opens the file and returns a list of frequency distributions
	# written within the read file
	def readOpFromFile(filename):
		pass
		return [[('',0)]]



	# takes in two lists
	# each list shall be of tuples
	# each tuple shall have a word in the first index and a frequency in the second index
	# method will manually compute and return the cosine similarity of the two vectors
	# each l# are frequency distribution vectors
	def compute_cosine_similarity(l1, l2):
		
		l1_extracted = [e[0] for e in l1] # extract words (index 0) from lists
		l2_extracted = [e[0] for e in l2]

		from_l1_add = [ (e[0], 0) for e in l1 if e[0] not in l2_extracted] # create list of tuples with zero counts for misses
		from_l2_add = [ (e[0], 0) for e in l2 if e[0] not in l1_extracted]

		# vectors should now be same length, add misses and sort
		l1 = sorted(l1 + from_l2_add) # sort alphabetically
		l2 = sorted(l2 + from_l1_add)

		v1 = [e[1] for e in l1] # extract word counts
		v2 = [e[1] for e in l2]

		v1 = np.array( v1, np.float) # convert to mathematical array
		v2 = np.array( v2, np.float)

		v1 = v1/la.norm(v1) # convert to unit vector
		v2 = v2/la.norm(v2)
		
		return np.dot(v1,v2) # compute dot product
		
		
		
##################          Graph Methods            #######################	
		
		
# Child
class DocumentGraph(Document):
	
## Instance Methods
# Call these like this: obj.func()		
	
    def __init__(self, filename, stpwords = []):
		super(filename)
		self.graph = None # needs replaced with method
	

## Static Methods
# Call these like this: comparison_tool.func()
	
	
	# TODO
	# This function opens the file and returns a list of graphs for comparison
	# It reads whatever a graph looks like when written witin a file
	def readOpFromFile(filename):
		pass
		return [['']]
	

		
		
