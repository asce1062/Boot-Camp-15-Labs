def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    # For very large numbers calculate the cross sum first and then check if the cross sum is a multiple of 3
    elif sum(map(int, str(number))) % 3 == 0:
        return 'Fizz'
    elif (number % 5 == 0):
        return 'Buzz'
    else:
        return number
