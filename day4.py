
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# How many different passwords within the range given in your puzzle input meet these criteria?

def possible_passwords(start, stop):
    possible_passwords = []
    for password in range(start, stop + 1):
        password_list = list(str(password))
        list_to_sort = password_list[:]
        list_to_sort.sort()
        repeat, ordered = False, False
        
        if password_list == list_to_sort:
            ordered = True
        
        previous_digit = password_list[0]
        for index in range(1, len(password_list)):
            if previous_digit == password_list[index]:
                repeat = True
            previous_digit = password_list[index]
        
        
        if repeat and ordered:
            possible_passwords.append(password)
    
    return possible_passwords

def remove_multiple_repeats(possible_passwords):
    revised_possible_passwords = []
    for password in possible_passwords:
        str_password = str(password)
        multiple_repeat = False
        previous_digit = str_password[0]
        digit_dictionary = {}
        for digit in str_password:
            if digit_dictionary.get(digit):
                digit_dictionary[digit] += 1
            else:
                digit_dictionary[digit] = 1
        values_list = list(digit_dictionary.values())
        double = False
        multiples = False
        for value in values_list:
            if value == 2:
                double = True
            if value > 2:
                multiples = True
        
        if (not double and not multiples) or (double and multiples) or (double and not multiples):
            revised_possible_passwords.append(password)
    return revised_possible_passwords
