
import sys

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]


## Main() function
def main():
    # Say we have a list of strings we want to sort by the last letter of the string.
    strs = ['Hooman','Amir','Yousef','Reza','Omid','Elen']
    ## Now pass key=MyFn to sorted() to sort by the last letter:
    print(sorted(strs, key=MyFn)) 




if __name__ == '__main__':
    main()