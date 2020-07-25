#!/bin/python3
import SETTINGS as s



# layer_1_classifier == KNN

# This module shall do the manage the classifier algorithm code
def execute_classifier():
	
	# 1) Read Document(s) From File
	## Input: File Name as String
	## Output: Document Contents as String
	
	
	# 2) Read the algorithm input data from file (only want to do this once)
	s.layer_1_classifier.readFromFile()

	
	### SOME FUTURE WRAPPER CODE ###
	# (Like for multiple layers)
	
	
	# 3) Execute the Particular Algorithm -- (KNN)
	## Input: Document Contents as String
	## Output: Category as String
	out = s.layer_1_classifier.classify()
	
	
	
	# 4) Print the output category
	print(out)
	
