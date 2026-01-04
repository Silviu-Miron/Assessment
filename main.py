"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""






import tui
import process
import exporter
import visual





# Defining main function

def main():
    tui.display_title("Disneyland Review Analyser")

    data = process.load_data("data/disneyland_reviews.csv")
    print("Dataset loaded successfully")
    print("Number of rows:", len(data))


    running = True
    while running:
        tui.display_main_menu()
        choice = input("Enter your choice:").upper()

        if choice =="A":
            view_data_menu(data)

        elif choice =="B":
            visualise_data_menu(data)

        elif choice =="C":
            exporter.export_menu(data)

        elif choice =="X":
            print("Exiting program")

        else:
            print("Invalid menu choice")
            running = False













if __name__ == '__main__':
    main()