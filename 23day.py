-4.9.6. Lambda Expressions¶
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(0)
42
f(1)
43

5. Data Structures
 - list.append(x), .extend(iterble), .remove(x), .pop([i]), .clear(), .index(x[,start[end]]), .sort(*,key=none,reverse=False), .reverse(), .copy

 5.1.1. Using Lists as Stacks¶ (use list.()  - Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list    
 5.1.2. Using Lists as Queues - lists are not efficient for this purpose - queue.popleft()

5.2. The del statement¶ -  pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list 
    del a[:]

5.3. Tuples and Sequences - Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking
5.4. Sets - A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

5.5 Dictionary - Sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 

            Set of key: value pairs,
            main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. 
