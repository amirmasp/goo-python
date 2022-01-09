
# dictionary formatting and working with Files


def main():
  mylist = []
  ## Dict Formatting using % and hash
  ## The % operator works conveniently to substitute values from a dict into a string by name:
  #hash = {}
 # hash['word'] = 'garfield'
  #hash['count'] = 42
  #s = 'I want %(count)d copies of %(word)s' % hash # %d for int, %s for string
  #print(s) # 'I want 42 copies of garfield'

  # Open the contents of the file foo.txt and 'r'ead' into it line by line
  f = open('/home/amirmasp/goo-py-ex/my_exercises/foo.txt', 'rU')
  for line in f:
    # print(line),
    x = line ## x is just a string 
    print(type(x))
    mylist.append(x) ## we add all line objects to a list
  print(mylist)
  f.close()    
  
  # open the file foo.txt and 'a'ppend a line into it
  #f = open('/home/amirmasp/goo-py-ex/my_exercises/foo.txt', 'a')
  #f.write("5)Now the file has more content!")
  #f.close()
  # and now read the new file
  #f = open('/home/amirmasp/goo-py-ex/my_exercises/foo.txt', 'rU')
  #print(f.read())
  #f.close()
  ## Also you can write to a file but NOTIC: using 'w' you overriding to file
  ## f = open('/home/amirmasp/goo-py-ex/my_exercises/foo.txt', 'w')
  ## f.write("Woops! I have deleted the content! And wrote new content. If you wanna append something use 'a' instead of 'w'")
  ## f.close()






## standard bolerplate
if __name__ == '__main__':
    main()