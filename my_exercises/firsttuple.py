## We want to read command line args using sys module
import sys

## A simple function which takes no argument and returns the command line args as a tuple
def Foo():
    myTuple = (sys.argv[1], sys.argv[2])
    return myTuple

## maii=n function starts
def main():
    # Checks if all commands line args entered by user
    if len (sys.argv) > 2:
        (userName, userAge) = Foo()
        print('Hello %s. I do not blieve you are %d!' %(userName, int(userAge)))
    else:
        print('You have not provided enough command line arguments to run this program.')    
    


## This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()