# This is the master branch of repository Git-test on my local machine.
# Learning git is fun!
def add(n1, n2):
    return n1 + n2



print("Hello world")


operations = {
   "+": add,
   "-" :"substract",
   "*" :"multiply",
   "/" :"divide",
   "%" :"modulo"
 }

n1 = int(input("what is the first number?: ")) 
  
for symbols in operations:
    print(symbols)
    
n2 = int(input("what is the first number?: "))
print(f"The first number is {n1}, second number is {n2}. Addition = {add(n1,n2)}")
print(add(n1,n2))

print("Great experiment")