import re
import sys


def main():
    str = 'an example word:cat !!'
    match = re.search(r'word:\w\w\w\s\S\W', str)
    # If-statement after search() tests if it succeeded
    if match:
        print('found', match.group()) ## 'found word:cat'
    else:
        print('did not find')

    ## Search for pattern 'iii' in string 'piiig'.
    ## All of the pattern must match, but it may appear anywhere.
    ## On success, match.group() is matched text.
    match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
    match = re.search(r'igs', 'piiig') # not found, match == None

    ## . = any char but \n
    match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

    ## \d = digit char, \w = word char
    match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
    match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"    


    str = 'purple alice-b@google.com monkey dishwasher'
    match = re.search(r'\w+@\w+', str)# This does not match email in the str
    if match:
      print(match.group())  ## 'b@google'
      
    match = re.search(r'[\w.-]+@[\w.-]+', str) # this pattern matches email inside str
    if match:
      print(match.group())  ## 'alice-b@google.com' 

    str = 'purple alice-b@google.com monkey dishwasher'
    match = re.search(r'([\w.-]+)@([\w.-]+)', str)
    if match:
      print(match.group())   ## 'alice-b@google.com' (the whole match)
      print(match.group(1))  ## 'alice-b' (the username, group 1)
      print(match.group(2))  ## 'google.com' (the host, group 2) 

    ## Suppose we have a text with many email addresses
    str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

    ## Here re.findall() returns a list of all the found email strings
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
    for email in emails:
      # do something with each found email string
      print(email ) 




if __name__ == '__main__':
    main()    