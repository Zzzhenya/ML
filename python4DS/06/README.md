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