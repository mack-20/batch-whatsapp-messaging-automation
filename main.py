from input_handler import *
from phone_number_utils import *
from message_sender import *


def main():
    print("Welcome")
    
    # Get person count
    person_count = get_person_count()

    # Get phone numbers
    phone_numbers = get_phone_numbers(person_count)

    # Get Message
    message = get_message()

    # Send Message at desired time
    print(screen_width, screen_height)

    send_message_to_users(phone_numbers, message)

if __name__ == "__main__":
    main()