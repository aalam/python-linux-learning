#2026Jan17 - Sat
- https://docs.python.org/3/tutorial/controlflow.html#special-parameters
    - Special parameters
    4.9.3.1. Positional-or-Keyword Arguments
        - If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.
    4.9.3.2. Positional-Only Parameters
        -  If positional-only, the parameters’ order matters, and the parameters cannot be passed by keyword.
           Positional-only parameters are placed before a / (forward-slash).
           The / is used to logically separate the positional-only parameters from the rest of the parameters.
           If there is no / in the function definition, there are no positional-only parameters.
    4.9.3.3. Keyword-Only Arguments
        - To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, 
        place an * in the arguments list just before the first keyword-only parameter.


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


Guidence for Argument:

    Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

    Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

    For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

#II - Labex - Create and Run a Python Script in VS Code - Lab completed


