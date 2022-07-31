## fizzbuzz - classic interview queation

### Problem

This is a classic 
> For numbers, which are multiple of both three and five, you say fizz, buzz. So it goes something like this. One, two, fizz, four, buzz, fizz, seven, eight, fizz, et cetera. And the first fizz buzz will be 15. 


### Warning - make sure you ace this one

Aparently a popular interview question
> So this is an example where we need to think carefully about our algorithm before just diving in and implementing it. In fact, fizz, buzz is a very common interview question. So make sure that if it comes up at an interview for you, that you ace it.

### My solution


I think I aced this one, wrote the solution straight out with only two minor errors
* My initial upper bound was 100 and 101 
* One minor syntax error i.e. missing :  after one of else statements

So both here is solution, which I think I just about ace'd

```
~/projects/algorithmic-thinking-with-python $ cat docs/fizzbuzz-my-solution.py
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
```
...
```
~/projects/algorithmic-thinking-with-python $ python3  docs/fizzbuzz-my-solution.py
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
31
32
fizz
34
buzz
fizz
37
38
fizz
buzz
41
fizz
43
44
fizzbuzz
46
47
fizz
49
buzz
fizz
52
53
fizz
buzz
56
fizz
58
59
fizzbuzz
61
62
fizz
64
buzz
fizz
67
68
fizz
buzz
71
fizz
73
74
fizzbuzz
76
77
fizz
79
buzz
fizz
82
83
fizz
buzz
86
fizz
88
89
fizzbuzz
91
92
fizz
94
buzz
fizz
97
98
fizz
buzz
~/projects/algorithmic-thinking-with-python $ 
```

