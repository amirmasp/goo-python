
import sys 
# import sys to use command line args

##***********************************************************************
## A function scalar() that takes a single numeric argument n, and returns a function.
def scalar(n):
    y = []
    def new_function(v): # you can define a function inside the called function and return the defined function as object
        print('scaller =',n)
        print('vector =', v)   
        #return [num * n for num in v] # list comprehension
        for elem in v:
            y.append(n * elem)
        return y    

    return new_function ## Note: returning function is W/O paranthesis ()
##***********************************************************************


##***********************************************************************
## To run this program:
## $ python3 fn_as_obj.py {number}
## $ python3 fn_as_obj.py 100
def main():
    v1 = [1,5,3]
    v2 =[10,20,30,40]
    if not sys.argv[1]:
        print('Enter a ineger number as command line argument')

    else:
        my_int = int(sys.argv[1]) # The argv[1] is a string but we need int
        ## Call to add_n(n) function returns a function and in python we can assign function directly to a variable, myFn here,
        myFn1 = scalar(my_int)
        myFn2 =scalar(my_int)
        # i = abs //example
        # print(i(-10)) 
        ## we know myFn take a vector v as an argument and return a new vector with the value for n added to each element of vector v 
        ##  new_vector = myFn(my_vector)
        print('new_v1 =',myFn1(v1))
        print('new_v2 =',myFn2(v2))
        new_scalar = int(input("please enter new scalar value: "))
        myFn3 = scalar(new_scalar)
        print('new_v3 =',myFn3([100,200,300,400,500,600,700,800,900,1000]))
##***********************************************************************           


##***********************************************************************
## we need this boilerplate to run the code in shell
if __name__ == '__main__':
   main() 
##***********************************************************************   