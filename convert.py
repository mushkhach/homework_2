amount = raw_input("Please input currency followed by amount")
def c_converter(amount): 
    if amount[0]=="$":
        return str(484*int(amount[1:]))+" AMD"
    elif amount[0]=="e":
        return str(538*int(amount[1:]))+" AMD"
    else:
        return "Please use $ or e sign in front"
print c_converter(amount)