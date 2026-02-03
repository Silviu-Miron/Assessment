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
            print("\nYou have chosen option A - View Data")
            view_data_menu(data)

        elif choice =="B":
            print("\nYou have chosen option B - Visualize Data")
            visualise_data_menu(data)

        elif choice =="C":
            print("\nYou have chosen option C - Export Data")
            exporter.export_menu(data)

        elif choice =="X":
            print("\nExiting program")
            running = False

        else:
            print("\nInvalid menu choice")
            running = True


# Create view_data_menu function
def view_data_menu(data):
    back = False
    while not back:
        tui.display_view_menu()
        choice = input("Enter your choice:").upper()

        if choice =="A":
            print("\nYou have chosen option A - View Reviews by Park")
            park  = input("Enter park name:")
            reviews = process.get_reviews_by_park(data,park)
            for r in reviews:
                print (r)

        elif choice =="B":
            print("\nYou have chosen option B - Number of Reviews by Park and Reviewer Location")
            park = input("Enter park name:")
            location = input("Enter location:")
            count = process.count_reviews_by_park_and_location(data, park, location)
            print("Number of reviews:", count)

        elif choice =="C":
            print("\nYou have chosen option C - Average Score per year by Park")
            park = input("Enter park name:")
            year = input("Enter year:")
            avg = process.average_rating_by_year(data, park, year)
            print("Average rating:", avg)

        elif choice =="D":
            print("\nYou have chosen option D - Average Score per Park by Reviewer Location")
            park = input("Enter park name:")
            location = input("Enter reviewer location:")
            avg = process.average_score_by_park_and_location(data, park, location)
            print("Average score:", avg)

        elif choice =="X":
            print("\nYou have chosen option X - Back to main menu")
            back = True

        else:
            print("Invalid menu choice")

# Create visualise_data_menu function
def visualise_data_menu(data):
    back = False
    while not back:
        tui.display_visual_menu()
        choice = input("Enter your choice: ").upper()

        if choice =="A":
            print("\nYou have chosen option A - Most Reviews by Park")
            counts = process.reviews_per_park(data)
            visual.pie_chart(counts)

        elif choice == "B":
            print("\nYou have chosen option B - Park Ranking by Nationality")
            park = input("Enter park name:")
            top10 = process.top_10_locations(data, park)
            visual.bar_chart_locations(top10, park)

        elif choice =="C":
            print("\nYou have chosen option C - Most popular Month by Park")
            park = input("Enter park name:")
            monthly = process.monthly_average_ordered(data, park)
            visual.bar_chart_months(monthly, park)

        elif choice =="X":
            print("\nYou have chosen option X - Back to main menu")
            back = True

        else:
            print("\nInvalid menu choice")





if __name__ == '__main__':
    main()