# 4th task - practicing for loops with range, statements and % operator 
import sys

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Lūdzu, ievadi vienu argumentu - skaitli")
    sys.exit(1)
else:
   n_value = int(sys.argv[1])

for i in range(1, n_value + 1):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzJazz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 7 == 0:
        print("Jazz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

