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



def main():
    tui.display_title("Disneyland Review Analyser")

    data = process.load_data("data/disneyland_reviews.csv")
    print("Dataset loaded successfully")
    print("Number of rows:", len(data))






if __name__ == '__main__':
    main()