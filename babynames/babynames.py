#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""



##***************************************************************************************************************
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  return_list =[] # this list will be returned,names data
  founde_year = 0 # this integer will be returned, year int
  myhash ={}  # Dictionary 
  input_file = open(filename,'rU') # This line will be exactly printed 
  for line in input_file: ## The standard for-loop works for text files, iterating through the lines of the inputfile
    ## each line is a string and you can use it for your re.search() method as string whose going to be searched 
    match_year = re.search(r'Popularity\sin\s(\d\d\d\d)', line) # be carefull do not put any space in regex pattern 
    ## puting paranthises around numbers(\d\d\d\d) gives access to that value using
    ##  match_year.group(1) to access exactly our int year
    if match_year: # we are looking for first occurance of regex pattern, so break if just founded it
      break
  if match_year:
    # match_year is a user-defined object 
    # but match_year.group() returns a string 
    #print('found', match_year.group()) # prints all matched pattern that it found 
    #print('found', match_year.group(1)) # prints ONLY the value part of matched pattern, that part whose usedThe parenthesis ( ) group mechanism in regex. 
    founde_year = match_year.group(1)     # That part is integer value we got it inside The parenthesis ( ) group mechanism
                                            # And assign it to a variable found_year
    #print(founde_year)   
  else:
    # We didn't find a year, so we'll exit with an error message.
    print('Couldn\'t find the year!\n') 
    sys.exit(1)

  # Feed the input-file text into findall(); it returns a list of tuples each tuple is containing 3 strings
  # each tuple is: (rank, maleName, femaleName)
  # Remember input_file.read() returns a single string of whole inputfile
  tuples = re.findall( r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', input_file.read()) 
  ## re.findall() takes two input:
  ## (the regex pattern, a string containing all file texts)
  ## And returns a list.  Our regex has 3 parenthesis ( ) group mechanism,one for integer /d ,
  ## two and three for male and female name strings. These 3 from each line group into a size of 3 tuple (rank, namem, namef)  
  ## it puts all tuples into a list and returns
  #print(type(tuples[1])) # prints tuple at index 1, the tuple's size is 3.
  #print(tuples[1]) ## prints tuple at index 1
  for tuple in tuples: # Now we can put all data into a dictionary. our tupples are all in this form :(int rank, str male, str female)
    myhash[tuple[1]] = tuple[0] # tuple[0] is rank, tuple[1] is male, tuple[2] is female.
    myhash[tuple[2]] = tuple[0]   # we are separating male and female of each tuple into dictionary 
    ## tuple1 = {'Isabella': 7, 'Oliver': 7}, so tuple1[0] is 7 
  #print('Dictionary:\n'),
  #print(myhash)
  input_file.close()
  return_list = sorted(myhash.items()) # myhash.items() returns a list of tuplues (name, rank) whose are keys and values of dictionary
  ## We want a list sorted by name
  ## function finally returns a tuple containing (int founde_year, list return_list)
  return (founde_year ,return_list) 
##***************************************************************************************************************


##***************************************************************************************************************
def MyFn(t): ## A healper function for custom sorting tuples in the list
  return t[-1]
##***************************************************************************************************************

##***************************************************************************************************************
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == 'summaryfile.txt':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  fileName = args[0] ## get the file name
  (year,data) = extract_names(fileName) # return value is a tuple containing (year, data ) which are assigned to year and data
  if summary: # if in command line asks to write in the file
    output_file = open('summaryfile.txt', 'w') # Be caution we are writing into summary.txt NOT baby.html
    output_file.write(year)
    output_file.write('\n')
    for t in data:
      output_file.write(t[0])
      output_file.write(' ')
      output_file.write(t[1])
      output_file.write('\n')
    output_file.close()  
    print ('summaryfile.txt created as output_data')
  else: # just print data
    print(year)
    for t in data: # data is a list of size two tuples (name, rank)
    #if d[0] == 'Ellen':
      print(t[0], t[1])        
 
##***************************************************************************************************************

  
##***************************************************************************************************************  
if __name__ == '__main__':
  main()
##***************************************************************************************************************  
