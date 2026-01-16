#2025Jan15 - learned from python doc about control - 

https://docs.python.org/3/tutorial/controlflow.html#

 pass statement does nothing.
 match statement takes an expression and compares its value to successive patterns given as one or more case blocks. 
  even functions without a return statement do return a value
  result = result + [a]

  Default Argument Values
   The default value is evaluated only once
   Keyword Arguments - 
    
    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


    all the following calls would be invalid:

    parrot()                     # required argument missing
    parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
    parrot(110, voltage=220)     # duplicate value for the same argument
    parrot(actor='John Cleese')  # unknown keyword argument


No argument may receive a value more than once
def function(a):
    pass

function(0, a=0)



