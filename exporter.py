
"""
This module is responsible to  demonstrating the OOP (Object-Oriented Program). The data output information about each park, including numbers of reviews, numbers of positive reviews.
The output provide option for TXT, CSV, and JSON formats.

"""




import csv
import json

#Create  main class
class ParkExporter:
    def __init__(self, data):
        self.data = data
        self.results = {}

    def prepare(self):
        for row in self.data:
            park = row["Branch"].strip()
            rating = int(row["Rating"])
            country = row["Reviewer_Location"]

            if park not in self.results:
                self.results[park] = {
                    "reviews": 0,
                    "positive": 0,
                    "rating_sum": 0,
                    "countries": []
                }

            # Update counters correctly
            self.results[park]["reviews"] += 1
            self.results[park]["rating_sum"] += rating

            if rating >= 4:
                self.results[park]["positive"] += 1

            if country not in self.results[park]["countries"]:
                self.results[park]["countries"].append(country)

#Inplement functionality for text export function
    def export_txt(self):
        file = open("export.txt", "w")

        for park in self.results:
            avg = self.results[park]["rating_sum"] / self.results[park]["reviews"]

            file.write("Park: " + str(park) + "\n")
            file.write("Reviews: " + str(self.results[park]["reviews"]) + "\n")
            file.write("Positive reviews: " + str(self.results[park]["positive"]) + "\n")
            file.write("Average rating: " + str(avg) + "\n")
            file.write("Countries: " + str(len(self.results[park]["countries"])) + "\n\n")

        file.close()

    def export_csv(self):
        file = open("export.csv", "w", newline="")
        writer = csv.writer(file)

        for park in self.results:
            avg = self.results[park]["rating_sum"] / self.results[park]["reviews"]
            writer.writerow([
                park,
                self.results[park]["reviews"],
                self.results[park]["positive"],
                avg,
                len(self.results[park]["countries"])
            ])

        file.close()

    def export_json(self):
        output = {}

        for park in self.results:
            avg = self.results[park]["rating_sum"] / self.results[park]["reviews"]
            output[park] = {
                "reviews": self.results[park]["reviews"],
                "positive": self.results[park]["positive"],
                "average_rating": avg,
                "countries": len(self.results[park]["countries"])
            }

        file = open("export.json", "w")
        json.dump(output, file, indent=4)
        file.close()


def export_menu(data):
    exporter = ParkExporter(data)
    exporter.prepare()

    print("\nPlease select export format:")
    print("[A] TXT")
    print("[B] CSV")
    print("[C] JSON")
    print("[X] Back to main menu")


    choice = input("Enter your choice: ").upper()

    if choice == "A":
        print("\nYou have chosen option A - TXT")
        exporter.export_txt()
        print("Exported to export.txt")

    elif choice == "B":
        print("\nYou have chosen option B - CSV")
        exporter.export_csv()
        print("Exported to export.csv")

    elif choice == "C":
        print("\nYou have chosen option C - JSON")
        exporter.export_json()
        print("Exported to export.json")

    elif choice == "X":
        print("\nYou have chosen option X - Back to main menu")

    else:
        print("Invalid choice")














