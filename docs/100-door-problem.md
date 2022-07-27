 ## 100 door problem

 ### Overview
 
 > Imagine you have 100 doors in a row that are all initially closed. you going to make 100 passes by each of these doors. And on the first pass, you going to visit each door in sequence and toggle it state. So that means if it's closed, it becomes open. If it's open, it becomes closed. Since all the doors are initially closed, this will result in all the doors being open after the first pass. For the second pass, you visit every second door and toggle it state. For the third pass, you visit every third door, and so on and so forth, until you only visit the 100th on the 100th pass.


### Test-01 - 3 door problem simplified problem

```
 ~/projects/algorithmic-thinking-with-python $ cat docs/100-door-problem-test-01.py
door_problem_size=3
door_problem_size=door_problem_size+1 ## ignoring the [0] place holder

doors = [False] * door_problem_size

print("Start: " + str(doors[1:]))
for mod_n in range(1,door_problem_size):
  print("*** round :" + str(mod_n)) 
  for i in range(1,door_problem_size): 
    if ( i % mod_n == 0):
      print (str(i) + ":" + str(mod_n))
      doors[i] =  not doors[i]
  print(doors[1:])
  print ()
    
print ("*** Final outcome:")
for i in range(1,door_problem_size):
    ## print(doors[i])
    if ( str(doors[i]) == 'True'):
      print (str(i))  
```
...
```
~/projects/algorithmic-thinking-with-python $ python3 docs/100-door-problem-test-01.py
Start: [False, False, False]
*** round :1
1:1
2:1
3:1
[True, True, True]

*** round :2
2:2
[True, False, True]

*** round :3
3:3
[True, False, False]

*** Final outcome:
1
```

### Test-02 - 4 door problem simplified problem

```
~/projects/algorithmic-thinking-with-python $ cat docs/100-door-problem-test-02.py
door_problem_size=4
door_problem_size=door_problem_size+1 ## ignoring the [0] place holder

doors = [False] * door_problem_size

print("Start: " + str(doors[1:]))
for mod_n in range(1,door_problem_size):
  print("*** round :" + str(mod_n)) 
  for i in range(1,door_problem_size): 
    if ( i % mod_n == 0):
      print (str(i) + ":" + str(mod_n))
      doors[i] =  not doors[i]
  print(doors[1:])
  print ()
    
print ("*** Final outcome:")
for i in range(1,door_problem_size):
    ## print(doors[i])
    if ( str(doors[i]) == 'True'):
      print (str(i))  
```
...
```
~/projects/algorithmic-thinking-with-python $ python3 docs/100-door-problem-test-02.py
Start: [False, False, False, False]
*** round :1
1:1
2:1
3:1
4:1
[True, True, True, True]

*** round :2
2:2
4:2
[True, False, True, False]

*** round :3
3:3
[True, False, False, False]

*** round :4
4:4
[True, False, False, True]

*** Final outcome:
1
4
```