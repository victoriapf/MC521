## the following code is in python ##

## The function makeChange: Iterate over the possible combinations of 
    # quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cents)
    # and save the correts convertions on a list
    # Input: an int to be converted
    # Output: an list with all the possible convertions 
def makeChange(total):
    _set = []
    for count25 in range(0, total):
        for count10 in range(0, total):
            for count5 in range(0, total):
                _sum = count25*25 + count10*10 + count5*5
                if (_sum <= total): # a sum of coins exists
                    # the number of pennies is known by default
                    count1 = total - _sum 
                    _set.append([count25,count10,count5,count1])
                elif count5 * 5 > total:
                    break
            if count10 * 10 > total:
                break
        if count25 * 25 > total:
            break

    return _set

## An example of the function calling
if __name__ == '__main__':
    print(makeChange(12))
