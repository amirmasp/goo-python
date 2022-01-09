#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
##*************************************************************************************
import sys
##*************************************************************************************

##*************************************************************************************
# define a helper function that reads a file and builds and returns a dictionary
def healper_function(filename):
  myfile= open(filename, 'rU') # myfile is a file objext 
  mystring = myfile.read() # myfile.read() method reads the whole of file into a single string mystring
  myfile.close() # We do not need file to be open anymore
  #print('original mystring: "%s"' %(mystring))
  mystring= mystring.lower() # store all the words as lowercase
  #print('lowercase mystring: "%s"' %(mystring))
  mylist = mystring.split() # mystring.split returns a list of substrings separated by the given delimiter
  #print('splitted strings from mystring go to a single list namely mylist :\n',mylist)
  myhash = {} # my dictionary to map between words and their occurance(counts)    hash:string--->int
  for word in mylist: # words in the mylist are our keys of the dictionary
    if word in myhash: # checks if the key is already in the myhash
      myhash[word] += 1 # then add 1 count to its value
      # myhash[word] returnes the value associated with the key,myhash[word], and adds up one to current value of this key
    else: # the word is not one of the keys in the dictionary, myhash, and is a new word   
      myhash[word] = 1  # assign one to the new key of your dictionary
  return myhash # returns the dictionary to whereever its called   
##*************************************************************************************  


##*************************************************************************************
# 1. print_words function acts like an interface and sorts(by words) and prints dicts items
def print_words(filename):
  myhash =  healper_function(filename) # calls healper function and gets a dictionary
  words = sorted(myhash.keys())
  for key in words: ## loop through the sorted keys in myhash
    print(key , myhash[key]) # print words and their occurances
##*************************************************************************************    
   
##**********************************************************************************
## Using in print_top() function to sorting with key=
## A little function that takes a tuple, and returns its last item. which in this case is the associated value to a key in a dictionary
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(t): # Takes a tupple as input
    return t[-1] # Returns the last element of that tuple to the proxi
                    # Finally sorted() function sorts that proxy 
##**********************************************************************************

##************************************************************************************* 
# 2. print_top() function which reads a file then calls to a healper function and takes back a dictionary
# and prints the top 20 most common words sorted so the most common word is first, then the next most common, and so on.
def print_top(filename):
  mydict = healper_function(filename) # calls healper function and gets a dictionary
  tuples =[] # I will create many tuples and store them in this list, tuples,
  newlist =[] # the custom sorted list  
  tuples = mydict.items() # returns a list of tuple contain (key, value)
  #print('tuples:',tuples) 
  #print("we just done a custom sotrting with using key=MyFn function, which shows the sorted list tuples, most using words in the given file is: ")
  #print(sorted(tuples, key=MyFn,reverse=True))
  newlist = sorted(tuples,key=MyFn,reverse=True)
  #print('newlist:',newlist)
   
  print('prints just the top 20 most common words sorted so the most common word is first, then the next most common, and so on.')
  for t in newlist[0:20]:
    print(t[0], t[1])

 
##*************************************************************************************


##*************************************************************************************
# Run this module from ubuntun:
# python3 wordcount.py --count small.txt 
# python3 wordcount.py --topcount small.txt
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file, argc =',len(sys.argv))
    sys.exit(1)

  print('argc =', len(sys.argv))  
  option = sys.argv[1]
  filename = sys.argv[2] ## with command line arg[2] we gave the location and name of the file
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)
##*************************************************************************************
    
##*************************************************************************************
if __name__ == '__main__':
  main()
##*************************************************************************************