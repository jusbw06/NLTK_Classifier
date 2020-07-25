#!/bin/python3
import argparse
import SETTINGS as s
from classifier import *



## This script shall take in details like the type of classifier and type of comparison algorithm as command like arguments
## This script shall take in a the filename of a single Document and use the selected classifier to output its appropriate category
## This is written for using a single document; mulitple document functionality will be added later
if __name__ == '__main__':

	# 1) Read in and process command line arguments
	parser = argparse.ArgumentParser(prog='classify-document', description='Places input document into category')
	parser.add_argument('--algorithm', dest='algorithm_type', choices=['KNN','NN','SVM'], type=str, default='KNN', help='The name of the Machine Learning Algorithm to be used by the program')
	parser.add_argument('--comparison', dest='comparison_type', choices=['vectorized','graph'], type=str, default='vectorized', help='chooses comparison method for comparative (KNN) algorithms')
	parser.add_argument(dest='document_filename', metavar='document_filename.txt', help='the name of the document to be classified')
	args = parser.parse_args()

	# 2) update Settings.py
	s.ALG = args.algorithm_type
	s.CMP = args.comparison_type
	s.DOC = args.document_filename
	s.update_program_state()

	# 3) call classifier.py with appropriate options
	execute_classifier()
