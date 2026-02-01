"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""



import matplotlib.pyplot as plt


# Define pie chart function
def pie_chart(data):
    plt.pie(data.values(), labels=data.keys(),autopct = "%1.1f%%")
    plt.title("Most Reviewed Parks")
    plt.show()

# Define bar chart location
def bar_chart_locations(data,park):
    plt.bar(data.keys(),data.values())
    plt.title("Top 10 Locations for" + park)
    plt.xticks(rotation=45)
    plt.show()

# Define bar char months
def bar_chart_months(data,park):
    plt.bar(data.keys(),data.values())
    plt.title("Average Monthly Rating for " + park)
    plt.xlabel("Month")
    plt.ylabel("Rating")
    plt.show()
