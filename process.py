"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""


import csv

# Defining load_data function
def load_data(filename):

    data = []
    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
    file.close()
    return data

# Create Functionality for reviews by park function
def get_reviews_by_park(data, park):
    result = []
    for row in data:
        if row["Breach"] == park:
            result.append(row)
    return result

# Implement functionality for count reviews by park and location function
def count_reviews_by_park_and_location(data,park, location):
    count = 0
    for row in data:
        if row["Branch"] == park and row["Reviewer_Location"] == location:
            count += 1
    return count

# Create functionality for rating by year function
def average_rating_by_year(data, park,year):
    total = 0
    count = 0
    for row in data:
        if row["Branch"] == park and row["Year_Month"].startswith(year):
         total += int (row["Rating"])
         count += 1

    if count == 0:
        return 0
    return total / count

# Review per park function
def reviews_per_park(data):
    result = {}
    for row in data:
        park = row["Branch"]
        if park not in result:
            result[park] = 0
        result[park] += 1
    return result

# top 10 location function
def top_10_locations(data,park):
    totals ={}
    counts = {}

    for row in data:
        if row["Branch"] ==park:
            loc = row["Reviewer_Location"]
            rating = int(row["Rating"])

            if loc not in totals:
                totals[loc]=0
                counts[loc] =0

            totals[loc] += rating
            counts[loc] += 1


    averages ={}
    for loc in totals:
        averages[loc]=totals[loc]/counts[loc]

    sorted_items = sorted(averages.items(),key=lambda x: x[1],reverse = True)

    top10 = {}
    limit = 0
    for item in sorted_items:
        if limit == 10:
            break
        top10[item[0]] = item[1]
        limit += 1
    return top10

# Monthly average ordered function
def monthly_average_ordered(data,park):
    month_names =[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]
    totals={}
    counts={}

    for row in data:
        if row["Branch"] == park:
            parts = row["Year_Month"].split("_")

            if len(parts) !=2:
                continue
            month_number = parts[1]

            if not month_number.isdigit():
                continue
            month_index = int(month_number)-1

            if month_index <0 or month_index >11:
                continue
            month_name =month_names[month_index]

            if month_name not in totals:
                totals[month_name]=0
                counts[month_name]=0


            totals[month_name] += int(row["Rating"])
            counts[month_name] += 1

    averages ={}
    for month in month_names:
        if month in totals:
            averages[month]=totals[month]/counts[month]
        else:
            averages[month]=0

    return averages























