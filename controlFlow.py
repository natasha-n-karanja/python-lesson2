#Control Flow
"""
CONTROL FLOW REFERS TO THE ORDER IN WHICH INDIVIDUAL STATEMENTS, INSTRUCTIONS OR FUNCTION CALLS ARE EXECUTED OR EVALUATED. YOU CAN CONTROL FLOW USING:
"""

#Conditional statements
"""
CONDITIONAL STATEMENTS IN PYTHON ALLOW YOU TO EXECUTE BLOCKS OF CODE BASED ON CERTAIN CONDITIONS.
"""

#if ... elif ... else
if True:
  print("This will execute")
elif False:
  print("This will print")
else:
  print("This is the last part to execute")

#Loops
"""
THEY ARE USED TO ITERATE OVER A SEQUENCE OF ELEMENTS OR EXECUTE A BLOCK OF CODE REPEATEDLY
"""

#For loop
#USED TO ITRATE OVER SEQUENCES (LIKE LISTS, STRINGS, RANGES)
for i in range(1,11):
  print(i)

#While loop
#RUNS AS LONG AS THE CONDITION IS TRUE
Count = 0
while Count < 5: #CONDITION
  print("Count is:", count)
  count += 1

#Functions
"""
THEY ALLOW YOU TO ENCAPSULATE REUSABLE PIECES OF CODE AND ENHANCE CODE MODULARITY
"""
def add_sum(a,b):
  return a + b
result = add_sum(10,20)
print(result)