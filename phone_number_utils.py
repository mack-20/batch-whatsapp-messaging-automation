import re

def is_valid_phone_number(phone_number):
    pattern = r'^\+[1-9]\d{1,14}$'
    return re.match(pattern, phone_number) is not None

def get_phone_numbers(person_count):
    phone_numbers = []
    attempts = 3

    # Loop until the specified number of phone numbers is reached
    print("NB: Make sure phone number is in this format, +123456789")
    for count in range(person_count):
        for attempt in range(attempts):
            phone_number = input(f"Please enter the phone number {count+1} (Attempt {attempt+1}/3): ")
            if is_valid_phone_number(phone_number):
                phone_numbers.append(phone_number)
                break # Valid number, exit the inner loop
            else:
                print("Invalid phone number format. Please include a '+' sign at the beginning.")
        else:
            print("Too many invalid attempts. Moving to the next phone number.")

    # Display phone numbers enterd, if array is not empty
    if phone_numbers:
        print("You have entered the following numbers")
        for phone_number in phone_numbers:
            print(phone_number)
    else:
        print("No valid phone number was entered.")
    return phone_numbers