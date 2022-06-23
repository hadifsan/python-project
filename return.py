num = input("input number for cube:")
def cube(num):
    return num*num*num # if no return statement, the cube(3) below will not be displayed


result = cube(float(num))
print("The answer is " + str(result)) # the value will go back to return statement
