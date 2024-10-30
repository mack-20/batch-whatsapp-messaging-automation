# WhatsApp Batch Messaging Automation

This Python program allows you to send the same message via WhatsApp to multiple phone numbers at a specified time. It supports user input for phone numbers, messages, and the scheduled time, and it handles basic input validation.

## Features

- Collects multiple phone numbers in a specified format.
- Accepts multi-line messages.
- Schedules messages to be sent at a specified hour and minute.
- Provides feedback on the status of message sending.
- Supports interrupting message entry with the ESC key.

## Requirements

- Python 3.x
- `pywhatkit` library
- `keyboard` library

You can install the required libraries using pip:

```bash
pip install pywhatkit keyboard
```

## Usage

1. **Run the Program**: Execute the script in your Python environment.
2. **Input Welcome Message**: A welcome message will be displayed.
3. **Input Count of Recipients**: Enter the number of users you want to send messages to.
4. **Input Phone Numbers**: Enter phone numbers in the format `+1234567890`. You will have three attempts to enter a valid phone number for each recipient.
5. **Input Your Message**: Type your message line by line. Press `ESC` followed by `ENTER` on an empty line to finish entering the message.
6. **Input Scheduled Time**: Specify the hour (0-23) and minute (0-59) at which to send the message.
7. **Message Sending**: The program will send the message to all entered phone numbers at the specified time.

## Functions

### `welcome_message()`

Displays a welcome message.

### `clear_screen()`

Clears the console screen and displays the welcome message.

### `listen_for_esc()`

Listens for the ESC key to be pressed and sets a flag to stop input collection.

### `is_valid_phone_number(phone_number)`

Validates the format of a phone number. The number must start with a '+' followed by 1-14 digits.

### `get_message()`

Prompts the user to enter a multi-line message. Ends input when the user presses `ESC` and then `ENTER` on a new empty line.

### `get_person_count()`

Prompts the user for the number of recipients and validates the input.

### `get_phone_numbers(person_count)`

Collects phone numbers from the user, validating each entry. Provides a maximum of three attempts for each phone number.

### `send_message_to_users(phone_numbers, message, hour, min)`

Sends the specified message to each phone number at the scheduled time using the `pywhatkit` library.

### `get_time()`

Prompts the user for the hour and minute at which to send the message and validates the input.

### `main()`

The main function that orchestrates the flow of the program.

## Example

```bash
$ python py-whatsapp.py
```

Follow the prompts to enter phone numbers, your message, and the time for sending.

## Notes

- Ensure you have WhatsApp Web logged in on your default web browser.
- The program uses `pywhatkit`, which automates sending messages through the web interface of WhatsApp.
- Make sure your computer is connected to the internet when running the program.

## License

This project is open source and available under the MIT License.
