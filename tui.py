"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""





# Create display_title function
def display_title(title):
    line = "_" * len(title)

    print(line)
    print(title)
    print(line)

# Define display_main_menu function
def display_main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")


# Define display_view_menu function
def display_view_menu():
    print("\n Please enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Back to Main Menu")

# Define display_visual_menu function
def display_visual_menu():
    print("\n Please enter one of the following options:")
    print("[A] Most reviewed Parks")
    print("[B] Parks Ranking by Nationality")
    print("[C] Most Popular Month by Park")