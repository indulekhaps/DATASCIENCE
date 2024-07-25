
mobile_number = input("Enter a 10 digit mobile number: ")
if len(mobile_number) == 10 and mobile_number.isdigit():
    all_digits = set('0123456789')
    number_set = set(mobile_number)
    absent_digits = sorted(all_digits - number_set)
    if absent_digits:
        print("The absent digits in the mobile number is", absent_digits)
    else:
        print("All digits from 0 to 9 are present in the mobile number")
else:
    print("Please enter a valid 10 digit mobile number.")