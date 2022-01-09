#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.


##**********************************************************************************
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  counter_number = 0
  for item in words:
    if len(item) >= 2 and item[0] == item[-1]:# for test case 2 which has a '' empty sting the first part of if len(item) >= 2 works
      counter_number += 1
  return counter_number

##**********************************************************************************


##**********************************************************************************
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  mylist = []
  xlist = []
  for item in words:
    if item.startswith('x'):
      xlist.append(item)
    else:
      mylist.append(item) 
  mylist.sort()
  xlist.sort()
  return xlist + mylist
  ## instead of last 3 lines you can use this:
  # return sorted(x_list) + sorted(other_list)

##**********************************************************************************


##**********************************************************************************
## Using in task C
## Write a little function that takes a tuple, and returns its last item.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(t): # Takes a tupple as input
    return t[-1] # Returns the last element of that tuple to the proxi
                    # Finally sorted() function sorts that proxy 
##**********************************************************************************


##**********************************************************************************
# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  print('list of tuples:', tuples)
  print('sorted list without using key function:', sorted(tuples))
  print('sorted list using key=MyFn function is:', sorted(tuples, key=MyFn))
  return sorted(tuples, key=MyFn)

##**********************************************************************************


##**********************************************************************************
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

##**********************************************************************************


##**********************************************************************************
# Calls the above functions with interesting inputs.
def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


  print('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), 
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])     

##**********************************************************************************


##**********************************************************************************
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()

##**********************************************************************************
