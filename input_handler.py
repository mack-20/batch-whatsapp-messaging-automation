import sys
import threading
import keyboard as kbd

stop_input = False

def listen_for_esc():
    global stop_input
    kbd.wait('esc') # Wait for the 'esc' key to be pressed
    stop_input = True # Set the flag to stop input collection

def get_message():
    print("Enter your message (press ESC + ENTER on a new empty line to finish): ")
    message_lines = []

    # Start the escape key listener in a seperate thread
    listener_thread = threading.Thread(target=listen_for_esc)
    listener_thread.daemon = True # Allows thread to exit when the main program exits
    listener_thread.start()

    while not stop_input:
        line = sys.stdin.readline() # Read from standard input
        if line.strip(): # Only add non-empty lines
            message_lines.append(line.strip()) # Strip whitespace
        else:
            print("Empty line, please enter text. [SAFE TO IGNORE]")

    return "\n".join(message_lines)



def get_person_count():
    # Prompt user
    person_count = input("How many users do you want to send this message to: ")

    # Convert the input to an integer
    try:
        person_count = int(person_count)
        print(f"Input received, you want to send the message to {person_count} account(s))")
    except ValueError:
        print(f"{person_count} is not a valid number")

    return person_count
