2026Jan20 - Labex
- UnicodeDecodeError
- try -  except
-  strict, ignore, replace, xmlcharrefreplace

#II - Understand Identifiers in Python
 - fundatmental rules governing how to name variable, functions, classes and other objects in Python code
 Naming Rules:
     -Identifiers a-z, A-Z, 0-9 or _
     -first character of identifer can't be a digit
     -identifier can't contain space or special character as @, %, $ or * etc
     -identifiers are case sensitive - Myvariable and myvariable are Different identifier
     -Pythong Keywords/built-in fuctions can't be used as identifiers
### underscore conventions:

Single leading underscore (_name): This convention indicates that the identifier is intended for _internal use within a module or class_. It's a hint to other programmers that they shouldn't directly access this identifier from outside the module or class. However, Python does not strictly enforce this; you can still access it if you choose.

Double leading underscore (__name): This convention is used for name mangling in _classes_. 
When an identifier within a class starts with two underscores (and doesn't end with two underscores), Python internally changes the name to make it __harder to access from outside the class directly__. This helps prevent naming conflicts in inheritance.


Double leading and trailing underscores (__name__): These identifiers are reserved for __special use by the Python interpreter.___ Examples include __init__ (constructor), __str__ (string representation), etc. You should avoid creating your own identifiers with this pattern unless you are implementing one of Python's special methods.


Single trailing underscore (name_): This convention is used to avoid naming conflicts with Python keywords. If you want to use a name that is a Python keyword (like class or for), you can append an underscore to make it a valid identifier (e.g., class_, for_).

