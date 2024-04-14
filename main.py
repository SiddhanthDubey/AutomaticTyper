from pynput.keyboard import Controller
import time


def type_text(text):
    time.sleep(3)
    keyboard = Controller()
    for char in text:
        keyboard.type(char)
        time.sleep(0.01)  # Adjust the delay between keystrokes if needed


def read_file_and_type(filename):
    with open(filename, 'r') as file:
        content = file.read()
        type_text(content)


# Example usage:
read_file_and_type('example.txt')
