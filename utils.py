class utils:
    def __init__(self, num):
        self.num = num

    def reversed(number):
        if(type(number.num) is int):
            numList = [str(x) for x in str(number.num)]
            numList.reverse()
            revNum = int("".join(numList))
            print("Initial number is " + str(number.num) +" and reversed number is " + str(revNum) + " \n")
            return revNum        
        else:
            print("Reversed Error: type of input is not an int. Please try again \n")
            return None

    def formatter(number):
        if(type(number.num) is int):
            binNum = bin(number.num)
            octNum = oct(number.num)   
            print("Initial number: " + str(number.num) +", number in binary: " + str(binNum) + ", number in octal: " + str(octNum) +" \n")
            return binNum, octNum
        else:
            print("Formatter Error: type of input is not an int. Please try again \n")
            return None
