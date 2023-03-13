#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
        
    print("Happy New Year!")
    pass

def square_integers(int_list):
    return [i ** 2 for i in int_list]
    pass

def fizzbuzz():
    i = 1
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else: 
            print(i)
    pass
