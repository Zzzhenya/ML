# List comprehensions

a concise way to create lists in Python


```[expression for item in iterable]```

expression → what you want to put in the new list

item → each element from the iterable

iterable → something you can loop over (list, range, etc.)


### without

```
squares_of_evens = []
for x in range(10):
	if (x % 2 == 0):
		squares.append(x**2)

```

### with

```
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
```


### generator expressions vs list comprehensions

* same syntax

* [] -> returns a list -> makes a list immediately in memory
* () -> returns a generator object -> <class 'generator'> -> memory efficient - already an iterator

iter([list comprehension]) -> returns iterator object

original filter() function evaluate lazy, - the main advantage of a filter object

using generator instead of a list makes it lazy


A filter object in Python is the iterator returned by the built-in filter() function. It represents a lazy sequence of elements from an iterable that satisfy a given condition.

Unlike a list, a filter object does not store all elements in memory; it generates each element on demand as you iterate over it.


## all vs any

all - return true if everything is true

any - return true if at least one is true


all (generator expression)

or 

all ([list comprehension])