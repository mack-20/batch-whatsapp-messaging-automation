import pywhatkit as kit
import time
from datetime import datetime, timedelta
import pyautogui
from tkinter import *

# Create a Tk instance
win = Tk()

# Hide the main window
win.withdraw()

# Get monitor screen resolution
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

def send_message(phone_number, message, hour, min, waiting_time):
    kit.sendwhatmsg(str(phone_number), message, hour, min, waiting_time, True, 2)
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964)
    pyautogui.click()
    pyautogui.press('enter')
    
    # Get the current time for the message sent
    sent_time = datetime.now().strftime("%A %d %B %Y at %H:%M")
    print(f"Message sent to {phone_number} on {sent_time}: \"{message}\" ")

def send_message_to_users(phone_numbers, message):
    for phone_number in phone_numbers:
        now = datetime.now()
        # Calculate the time for the next message
        scheduled_time = now + timedelta(minutes=1)
        hour = scheduled_time.hour
        minute = scheduled_time.minute

        send_message(phone_number, message, hour, minute, 25)
        time.sleep(2)