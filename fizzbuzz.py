for i in range(1, 100):

 number = int(input("Enter a number: "))

if number % 3 == 0 :
    print("Fizz")
elif number % 5 == 0 :
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0 :  
    print("FizzBuzz")
else:
    print(number)