#!/usr/bin/python3
# ====================================
# Title: Chicken to Hex Compiler
# Author: Ryan J. Slater
# Date: 08/02/2019
# Purpose: Compile Chicken into Hex for ChickenOS
# ====================================

import sys
import os


def intToHex(value):
    value = int(value)
    value = str(hex(value))[2:]
    value = (4 - len(value)) * '0' + value
    return value.upper()


def printHelp():
    bold = '\033[1m'
    normal = '\033[0m'
    print(bold + 'NAME' + normal)
    print(7 * ' ' + 'Cool Chicken Compiler')
    print()
    print(bold + 'SYNOPSIS' + normal)
    print(7 * ' ' + './ccc.py [ ' + bold + '-h' + normal + ' ] [ ' + bold + '-o' + normal + ' outfile' + ' ] [ ' + bold + '-w' + normal + ' wrapping' + ' ] [ ' + bold + '?' + normal + ' ] infile')
    print()
    print(bold + 'DESCRIPTION' + normal)
    print(7 * ' ' + 'This compiler takes raw chicken code and boils it into a nicely formatted .egg file of mini hex codes.')
    print()
    print(bold + 'COMMAND LINE OPTIONS' + normal)
    print(7 * ' ' + '-h , -? , --help')
    print(14 * ' ' + 'Display this help menu')
    print(7 * ' ' + '-o , --output')
    print(14 * ' ' + 'Specify the output file. Defaults to "laid.egg"')
    print(7 * ' ' + '-w , --wrapping')
    print(14 * ' ' + 'Specify how many hex values to output per line. Defaults to 16')
    print()


def parseArgs():
    # Check for a help flag
    if '-h' in sys.argv or '--help' in sys.argv or '-?' in sys.argv:
        printHelp()
        sys.exit()

    # Prep args, remove ccc.py, make sure we have an odd amount of args
    args = sys.argv[1:]
    if len(args) % 2 != 1:
        print('Invalid parameters')
        sys.exit()

    # Get input file
    cleanedArgs = {'input': args.pop(len(args) - 1)}
    if not os.path.exists(cleanedArgs['input']):
        print("Input filepath doesn't exist")
        sys.exit()
    elif not os.path.isfile(cleanedArgs['input']):
        print("Input filepath isn't a file")
        sys.exit()

    # Default values of arguments
    cleanedArgs['output'] = 'laid.egg'
    cleanedArgs['wrapping'] = 16

    # Parse through the args
    for i in range(0, len(args), 2):
        if args[i] in ['-o', '--output']:
            cleanedArgs['output'] = args[i + 1]
        elif args[i] in ['-w', '--wrapping']:
            try:
                cleanedArgs['wrapping'] = int(float(args[i + 1]))
            except:
                print('Output wrapping flag is invalid')
                sys.exit()
        else:
            print('Invalid parameters')
            sys.exit()

    return cleanedArgs


if __name__ == '__main__':
    # Fetch command line arguments
    args = parseArgs()

    # Get the chicken count per line in input file
    numChickens = []
    for line in open(args['input'], 'r'):
        if line[0] != '#':
            numChickens.append(line.lower().count('chicken'))

    # Write to output
    output = open(args['output'], 'w')
    currentLineCounter = 0
    for i, count in enumerate(numChickens):
        output.write(str(intToHex(count)))
        currentLineCounter += 1

        # Add space or newline depending on wrapping
        if currentLineCounter < args['wrapping']:
            output.write(' ')
        else:
            output.write('\n')
            currentLineCounter = 0

    # Write file
    output.close()
