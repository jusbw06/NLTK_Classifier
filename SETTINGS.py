#!/bin/python3
## This module handles global variables and options
import sys, os

# This module will cause the switching between different algorithms and
#  methods to go largely unnoticed in the background


# Global Variables
ALG = ''
CMP = ''
DOC = ''
layer_1_classifier = None
DocumentTool = None



# Functions
def update_program_state():
	
	# Variables to be set
	global layer_1_classifier
	global comparison_tool

	# Choose the Classifier
	if ALG=='KNN':
		sys.path.append(os.getcwd() + '/KNN')
		import KNN
		layer_1_classifier = KNN.Classifier
	elif ALG=='NN':
		sys.path.append(os.getcwd() + '/NN')
		import NN
		layer_1_classifier = NN.Classifier
	elif ALG=='SVM':
		sys.path.append(os.getcwd() + '/SVM')
		import SVM
		layer_1_classifier = SVM.Classifier
	
	# Choose the Document Comparison Import
	sys.path.append(os.getcwd() + '/Document')
	import Document
	if CMP=='vectorized':
		DocumentTool = Document.DocumentVectorized # needs update in future 
	elif CMP=='graph':
		DocumentTool = Document.DocumentGraph
# (Note, need to change os.getcwd() in future)
