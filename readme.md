## Exceptions:
Statement or expression that is syntactically correct but can give error when trying to execute it.

Exception traceback -> review that part

try:
    code
except:
    code to request correction

You can also specify an error type

try:
    code to divide two numbers

except ValueError:
    code
except ZeroDivisionError:
    code
except:
    code for any error
else:
    code that executes if there have bee no errors
    
    
##Conditional Execution
if, elif, else

in a while loop:
if you use break, the code after break but inside the loop will NOT be executed
if you use a boolean, the code after setting it to false will be executed!!

continue means go back to the beginning of the while

