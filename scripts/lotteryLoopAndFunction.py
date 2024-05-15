import random


def genLotNumbers(bet):
    print()
    print("**********************************")
    print("Here are the generated lotteries:")
    print("**********************************")

    for i in range(bet):
        numbers = random.sample(range(1, 50), 6)
        numbers.sort()
        for number in numbers:
            print("%2d" % number, end=" ")
        print()


print("How many lotteries do you want?")
n = int(input("The maximun is 4 lotteries => "))

print()
while n < 1 or n > 4:
    n = int(input("Sorry, the maximum is 4 lotteries. Please input again => "))

genLotNumbers(n)
