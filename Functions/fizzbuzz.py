def fizz_buzz(max_num):
    
    num_range = range(max_num)
    num_list = list(num_range)
    
    for num in num_list:    
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    return num
print(fizz_buzz(25))