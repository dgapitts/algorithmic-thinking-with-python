 ## 100 door problem

 ### Overview
 
 > Imagine you have 100 doors in a row that are all initially closed. you going to make 100 passes by each of these doors. And on the first pass, you going to visit each door in sequence and toggle it state. So that means if it's closed, it becomes open. If it's open, it becomes closed. Since all the doors are initially closed, this will result in all the doors being open after the first pass. For the second pass, you visit every second door and toggle it state. For the third pass, you visit every third door, and so on and so forth, until you only visit the 100th on the 100th pass.


### Test-01 - 3 door problem simplified problem - outcome [True, False, False]

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

### Test-02 - 4 door problem simplified problem - outcome  [True, False, False, True]

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

### Test-03 - 5 door problem simplified problem - outcome [True, False, False, True, False]

```
~/projects/algorithmic-thinking-with-python $ diff docs/100-door-problem-test-02.py docs/100-door-problem-test-03.py
1c1
< door_problem_size=4
---
> door_problem_size=5
```
...
```
~/projects/algorithmic-thinking-with-python $ python3 docs/100-door-problem-test-03.py
Start: [False, False, False, False, False]
*** round :1
1:1
2:1
3:1
4:1
5:1
[True, True, True, True, True]

*** round :2
2:2
4:2
[True, False, True, False, True]

*** round :3
3:3
[True, False, False, False, True]

*** round :4
4:4
[True, False, False, True, True]

*** round :5
5:5
[True, False, False, True, False]

*** Final outcome:
1
4
```

Test04 - interesting ...

```
      nothing added to commit but untracked files present (use "git add" to track)
~/projects/algorithmic-thinking-with-python $ cat docs/100-door-problem-my-solution.py
door_problem_size=100
door_problem_size=door_problem_size+1 ## ignoring the [0] place holder

doors = [False] * door_problem_size

print("Start: " + str(doors[1:]))
for mod_n in range(1,door_problem_size):
  #print("*** round :" + str(mod_n)) 
  for i in range(1,door_problem_size): 
    if ( i % mod_n == 0):
      #print (str(i) + ":" + str(mod_n))
      doors[i] =  not doors[i]
  #print(doors[1:])
  print ()
    
print ("*** Final outcome:")
for i in range(1,door_problem_size):
    ## print(doors[i])
    if ( str(doors[i]) == 'True'):
      print (str(i))  

~/projects/algorithmic-thinking-with-python $ ./docs/100-door-problem-my-solution.py
-bash: ./docs/100-door-problem-my-solution.py: Permission denied
~/projects/algorithmic-thinking-with-python $ python3 docs/100-door-problem-my-solution.py
Start: [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

...
*** Final outcome:
1
4
9
16
25
36
49
64
81
100
```


##  100-door-problem my-first-solution

```
~/projects/algorithmic-thinking-with-python $ cat docs/100-door-problem-my-solution.py
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
```
...
```
~/projects/algorithmic-thinking-with-python $ time python3 docs/100-door-problem-my-solution.py 
*** Final outcome:
1
4
9
16
25
36
49
64
81
100

real	0m0.062s
user	0m0.032s
sys	0m0.014s
```


### 100-door-problem more efficient solution

So this is the textbook answer from the instructor, I didnt concider the `step` param in `for i in range( start , stop , step )` which is fairly obvious and once it is pointed out, you can't not see it (but I'm still happy enought with my functional quick/first attempt)


```
~/projects/algorithmic-thinking-with-python-foundations-2450259 $ git checkout remotes/origin/01_02
Previous HEAD position was cf4871c Start of video.
HEAD is now at d88e831 Recorded successfully.
~/projects/algorithmic-thinking-with-python-foundations-2450259 $ cat 01_01/100_doors_solution.py 
doors = [False] * 101  # So we can start at door no. 1 We will ignore index 0.

for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

for i in range(1, 101):
    if doors[i] is True:
        print(i, end=", ")
```

```
~/projects/algorithmic-thinking-with-python-foundations-2450259 $ time python3 01_01/100_doors_solution.py
1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 
real	0m0.141s
user	0m0.048s
sys	0m0.033s
```
