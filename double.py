def double(n):  #4. pass the data into the function via its PARAMETERS
    return n * 2 # 5. return


userstring = input("Number please:")# 1. request user input
usernum = int(userstring) # 2. convert to an integer

print(double(usernum)) # 3, call the function with an argument
