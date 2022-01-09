# first list code
def main():
  list = ['larry', 'curly', 'moe']
  print(list, ' length is: ', len(list))

  list.append('shemp')         ## append elem at end
  print(list, ' length is: ', len(list))
  
  list.insert(0, 'xxx')        ## insert elem at index 0
  print(list, ' length is: ', len(list))
  
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print(list, ' length is: ', len(list))


  print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print('"curly" was founded in the list at index:', list.index('curly') )
  if 'lolo' in list: 
    print(list.index('lolo'))
  else:
    print('"lolo" is not in this fucking list Dude! But we did not get ValueError!!!')

  list.remove('curly')         ## search and remove that element
  print(list, ' length is: ', len(list))

  list.pop(1)                  ## removes and returns 'larry'
  print(list, ' length is: ', len(list))
  

if __name__ == '__main__':
    main()    
