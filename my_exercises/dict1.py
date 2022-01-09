
## dictionary and hash table methods and techniques

def main():
  ## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['o'] = 'omega'
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  
  print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
  ## .items() is the dict expressed as (key, value) tuples
  ## and returns a list of key/value tuples! which can be sorted()
  print(sorted(dict.items()))

  print(dict['a'])     ## Simple lookup, returns 'alpha'
  dict['a'] = 6       ## Put new key/value into dict
  if 'a' in dict:
    print("the value associated with 'a':", dict['a']) 
  else:
    print("'a' is not a key in dictionary dict") 
  ## using dis statement avoids KeyError 
  if 'z' in dict:
    print("the value associated with 'z':", dict['z']) 
  else:
    print("'z' is not a key in dictionary dict") 
  ## Also you can use this method 
  print(dict.get('g'))
  print(dict.get('b'))## None (instead of KeyError)  


  ## By default, iterating over a dict iterates over its keys.
  ## Note that the keys are in a random order.
  for key in dict: print(key)

  ## Exactly the same as above
  for key in dict.keys(): print(key)

  ## Get the .keys() list:
  print(dict.keys()) 
  keylist = dict.keys()
  print(sorted(keylist)) 
  ## As long as you got a list you can apply all lists method to it
  ## Likewise, there's a .values() list of values
  print(dict.values())
  


  ## Common case -- loop over the keys in sorted order,
  ## accessing each key/value
  for key in sorted(dict.keys()):
    print(key, dict[key]) ## print(key, value)


## This loop syntax accesses the whole dict by looping
  ## over the .items() tuple list, accessing one (key, value)
  ## pair on each iteration.
  for k, v in dict.items():
    print(k, '>', v)
   
  
  

## standard bolerplate
if __name__ == '__main__':
    main()