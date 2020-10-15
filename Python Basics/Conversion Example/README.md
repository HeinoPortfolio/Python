# IS211_Assignment6

The command to run the program is:  python tests.py


You can also run using nosetests but it will only indicate if they passed with an "ok".

I have included tests for the raise exception that is required in the assignent.  It is displayed as the first item in the output.  I solved the problem with converting the units by looking at it as a generic function composed of a series of variables in the form: [value + a] * b + c.  Where value is the unit to be converted and the rest are variables that take on a value whether or not they are pertinent to that particular equation.  So by substituting the appropriate values you can "turn on" or "turn off" different parts of the equation. 
