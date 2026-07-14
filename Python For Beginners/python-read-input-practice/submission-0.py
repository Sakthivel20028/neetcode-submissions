def add_two_numbers() -> int:
    ip = input()
    strings = (ip.split(","))
    
    sum = 0;
    for string in strings:
        sum = sum + int(string)
    return sum    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
