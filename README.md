# Python Assessment 

## Project Overview
 The Disneyland Review Analyser is a Python-based console application developed as part of academic assessment.
 The program reads a datasets of Disneyland reviews from a CVS file and allow that user to:

-View and analyse reviews data
-Visualise insights using charts
-Export aggregated results in multiple formats

The application is menu-driven and runs continuously until the use chooses to exit.


## Dataset

-File:disneyland_reviews.csv
-Format:CSV
-Loaded into:A list of dictionaries
-Key fields used:
   -Branch
   -Rating
   -Reviewer_Location
   -Year_Month

The dataset is loaded once at program start


## Program Structure

The project is split into multiple Python files to improve readability and modularity

Assessment/
|
|- main.py
|-process.py
|-visual.py
|-exporter.py
|-data/
|  |-disneyland_reviews.csv
|-README.md

## File Responsibility

### main.py
-Entry point of the program
-Display the main menu
-Control program flow
-Call functions from other modules

### tui.py (Text user Interface)

-Display all menus and titles
-Ensures consistent console formatting
-Contains no data processing logic

### process.py
Handles all data processing tasks, including:

-Loading CVS data
-Filtering reviews by location
-Counting reviews by location
-Calculating average ratings
-Computing monthly averages
-Finding top 10 reviewer locations

### exporter.py
Handles exporting aggregated data:

-TXT export
-CSV export
-JSON export

Exports include:

-Number of reviews per park
-Number of positive reviews(rating >=4 )
-Average rating
-Number of reviewer countries

## Program Flow

[A] View Data
[B] Visualise Data
[C] Export Data
[x] Exit

# View Data Menu

[A] View Reviews by Park
[B] Number of Reviews by Park and Reviewer Location
[C] Average Score per Year by Park
[D] Average Score per Park by Reviewer Location
[E] Back to Main Menu

# Visualise Data Menu

[A] Most Reviewed Parks
[B] Park Ranking by Nationality (Top 10 Locations)
[C] Moat Popular Month by Park

# Export Data Menu

[A] TXT
[B] CSV
[C] JSON


## Key Features

-Continuous menu execution
-Input validation for menu choice
-Modular design
-Beginner-friendly Python syntax
-Graphical visualisation
-Defensive handling of invalid data


## How to Run the Program

1. Ensure Python 3 is installed
2. Install required library: pip install matplotlib
3. Navigate to the project directory
4. Run python main.py


## Assumptions and Limitations
-Dataset format is consistent
-Rating are numeric integers
-Program runs in a console environment
-No external database connections is used


## Academic Integrity Statement
This project was developed for educational purpose only.
All code was written to demonstrate understanding of :

-Python fundamentals
-Functions and modules
-File handling
-Data structures
-Basic data visualisation


## Author

Student:[Silviu Miron]
Module: Problem-Solving Through Programming
Institution:[Solent University]
Academic Year:[Year One]





