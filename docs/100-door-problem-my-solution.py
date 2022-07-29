door_problem_size=100
door_problem_size=door_problem_size+1 ## ignoring the [0] place holder

doors = [False] * door_problem_size

##print("Start: " + str(doors[1:]))
for mod_n in range(1,door_problem_size):
  #print("*** round :" + str(mod_n)) 
  for i in range(1,door_problem_size): 
    if ( i % mod_n == 0):
      #print (str(i) + ":" + str(mod_n))
      doors[i] =  not doors[i]
  #print(doors[1:])
  ## print ()
    
print ("*** Final outcome:")
for i in range(1,door_problem_size):
    ## print(doors[i])
    if ( str(doors[i]) == 'True'):
      print (str(i))  

