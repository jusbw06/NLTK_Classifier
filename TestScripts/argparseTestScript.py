import argparse
import os
import sys

parser = argparse.ArgumentParser(prog='classify-document', description='Places input document into category')

parser.add_argument('--algorithm', dest='algorithm_type', choices=['KNN','NN','SVM'], type=str, default='KNN', help='The name of the Machine Learning Algorithm to be used by the program')

parser.add_argument('--comparison', dest='comparison_type', choices=['vectorized','graph'], type=str, default='vectorized', help='chooses comparison method for comparative (KNN) algorithms')

parser.add_argument(dest='document_filename', metavar='document_filename.txt', help='the name of the document to be classified')

args = parser.parse_args()
#print(args.algorithm_type)
#print(args.comparison_type)
#print(args.document_filename)

print(os.getcwd() + '/ExampleLib')
