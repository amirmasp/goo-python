## MIT 6.036 ML course Self-Assessment Exercises in python

##*****************************************************************
# Given two lists of numbers, write a procedure that returns
# a list of the element-wise sum of the number in those two lists.
# In the following, no imports should be used.
def add_two_list(a,b):
    ## A nice modern pythonic way to do this task using list comprehensions 
    ## [ expr for var in list ]
    newlist = [a[i] + b[i] for i in range(len(a))]
    return newlist
##*****************************************************************


##*****************************************************************
## Given two column vectors (each represented as a list of numbers),
## write a procedure dot that returns the (scalar) dot product
# # of two input vectors, each represented as a list of numbers.
def dot(v1,v2):
    dot_p = 0
    # I like this for loop
    for i in range(len(v1)):
        dot_p += v1[i] * v2[i]

    return dot_p
##*****************************************************************


##*****************************************************************
## main() function
def main():
    list1 = [1,2,3,4,5]
    list2 = [3,4,5,6,7]
    element_wise_list = add_two_list(list1, list2)
    dot_product = dot(list1, list2)
    print('Element wise list is:',element_wise_list)
    print('dot product is:', dot_product)
##*****************************************************************


##*****************************************************************
## boilerplate
if __name__ == '__main__':
    main()
##*****************************************************************    