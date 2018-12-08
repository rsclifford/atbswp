'''
Created on Dec 8, 2018

@author: rsclifford
'''
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')