#create a game call fizzbuzz 
#program should print numbers from 1 to 100
#nut if the number is divisible by 3, it should print "fizz"
#if the number is divdisible by 5, it should print "buzz"
#but if the number is divisible by both 3 and 5, it should print "fizzbuzz"
#else it should print the actual number 

for number in range (1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")

    elif number % 3 == 0:
        print("fizz")

    elif number % 5 == 0:
        print("buzz")

    else:
        print(number)    