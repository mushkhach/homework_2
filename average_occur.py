numbers=input("Enter your numbers")
argument=input("enter your argument")
def average(numbers):
    return  float(sum(numbers[-(argument):]))/float(int(argument))
print average(numbers)