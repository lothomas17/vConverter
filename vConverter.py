
import sys, os
import inspect
import json
import getpass
import re

from ConfigParser import SafeConfigParser
import argparse
from gooey import Gooey
from gooey import GooeyParser

tasks = []

#Sets up the paramters and filename
# parser=SafeConfigParser()
# parser.read('config.ini')
# OPTIONS=parser.get('PARAMETERS','params')
# FILENAME=parser.get('FILENAME','file_name')

# OPTIONS = OPTIONS.split(',')

# tempWord = OPTIONS[0]
# tempWord = " " + tempWord
# OPTIONS[0] = tempWord




def usage():
    print
    print "Usage:"
    print
    print "    >> python vConverter.py "
    print
    print
    print "Make sure that you have correctly filled out the configuration file that is included with this script!"


def beginParse(toRead):
    word = toRead
    length = len(word)
    listOfWords = word.split(",")

    return listOfWords


def run(args):
    #Opens the file indicated by the config file
    f = open(args. Filename, 'r')
    outputF = open('output.txt', 'w')

    print "Processed Arguments"

    while(True):
        #grabs a line from the text, and formats it correctly
        string = f.readline()
        if not string: break
        
        string = string.rstrip()
        string = string.replace("n,", "n;")

        string = " " + string

        words = beginParse(string)

        length = len(args.Parameters)
        wordlen = len(words)

        output = []

        #builds the output vector by adding ones for present elements
        for k in range(length):
            output.append(0)

        for i in range(0,wordlen):
            #print words[i]  
            if(words[i] in args.Parameters):
                indexToAdd = args.Parameters.index(words[i])
                output[indexToAdd] = 1

        
        if(len(output) < length):
            remainder = length - len(output)
            for j in range(remainder):
                output.append(0)

        #writes the output of the conversion to a file output.txt
        toWrite = str(output)
        toWrite = toWrite[1:]
        toWrite = toWrite[:-1]
        outputF.write(toWrite + '\n')

    f.close()
    outputF.close()
    print "Finished :-)"

@Gooey
def main():
    #Grabs the command line arguments, params and the Filename to be read
    parser = GooeyParser(description = "A converter from data to vectors.")
    parser.add_argument("Parameters", help = "The list of params that the input will be checked against.")
    parser.add_argument("Filename", help = "The name of the file that stores the input.", widget = 'FileChooser')
    args = parser.parse_args()

    #Parses the list of parameters correctly
    args.Parameters = args.Parameters.split(',')
    tempWord = args.Parameters[0]
    tempWord = " " + tempWord
    args.Parameters[0] = tempWord

    #Checks for invalid inputs
    if(len(sys.argv) < 1):
        usage()
        exit(1)
    print "Grabbed Arguments"
    run(args)


if __name__ == "__main__":
    nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdout = nonbuffered_stdout
    main()

