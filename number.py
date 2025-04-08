def number(num):
    if num > 0:
        print(f"{number} is positive!")
    elif  num < 0:
        print(f"{number} is negative!")
    else:
         print(f"{number} is zero!")

numb = float(input("Enter a number: "))
number(numb)