variable = 10 # The code is defining a variable called `variable` and assigning it a value of 10.

def modify_global(): # The code is defining a function called `modify_global()` that modifies the value of the global variable `variable`. 
                     # By using the `global` keyword, it allows the function to access and modify the global variable instead of creating a new local variable with the same name. 
                     # In this case, the function sets the value of `variable` to 20.
    global variable
    variable = 20

def main(): # The code is defining a function called `main()` that prints the value of the global variable `variable` before and after calling the `modify_global()` function.
    print("Before calling the function, variable =", variable)
    modify_global()
    print("Modifying global variable")
    print("After calling the function, variable =", variable)

if __name__ =="__main__": # The code is calling the `main()` function if the script is executed directly.
    main() 
