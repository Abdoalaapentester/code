
def fibonatcci(number):
    # assert number <= 0 and int(number) != number , "out of range"

    if number == 0 or number == 1:
        return number
    else:
        return fibonatcci(number -1) + fibonatcci(number - 2)

print(fibonatcci(8))