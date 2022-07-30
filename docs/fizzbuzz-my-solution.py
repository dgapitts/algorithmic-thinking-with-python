fizzbuzz_size=100

for i in range(1,fizzbuzz_size+1): 
  if ( i % 3 == 0):
    if ( i % 5 == 0):
      print("fizzbuzz")
    else:
      print("fizz")    
  else:
    if ( i % 5 == 0):
      print("buzz")
    else:
      print(i)  
    
