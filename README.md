# Python-Course-PITP-MUET
# Project Name: Student Marks Analyzer Toolkit 


# Student.CSV file 
Name,Subject,Marks
Ali,Math,78
Sara,Science,85
Ahmed,English,92
Ayesha,Math,65
Bilal,Science,0
Hina,English,88
Omar,Math,70
Zara,Science,95

# data loader file 
import csv

def read_csv(filepath):
    data = []
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
# data cleaner file
def drop_missing(data, column):
    """Remove rows with missing or invalid values in a given column"""
    return [row for row in data if row[column].strip() != '' and row[column].strip().isdigit()]

def fill_missing(data, column, value):
    """Fill missing values in a column with a default value"""
    for row in data:
        if row[column].strip() == '' or not row[column].strip().isdigit():
            row[column] = str(value)
    return data
    
    
# data Analyzer file 
import statistics

def mean(data, column):
    marks = [int(row[column]) for row in data]
    return statistics.mean(marks)

def median(data, column):
    marks = [int(row[column]) for row in data]
    return statistics.median(marks)

def mode(data, column):
    marks = [int(row[column]) for row in data]
    return statistics.mode(marks)

def maximum(data, column):
    marks = [int(row[column]) for row in data]
    return max(marks)

def minimum(data, column):
    marks = [int(row[column]) for row in data]
    return min(marks)
# data visualise file 
import matplotlib.pyplot as plt

def plot_histogram(data, column):
    marks = [int(row[column]) for row in data]
    plt.hist(marks, bins=10)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()

def plot_bar_chart(data):
    names = [row['Name'] for row in data]
    marks = [int(row['Marks']) for row in data]
    plt.bar(names, marks)
    plt.title("Student Marks Comparison")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.xticks(rotation=45)
    plt.show()
    
# data report generator file
def data_summary(data):
    total = len(data)
    empty = sum(1 for row in data if row['Marks'].strip() == '' or not row['Marks'].isdigit())
    non_empty = total - empty
    print("\n Data Summary Report:")
    print(f"Total Records     : {total}")
    print(f"Valid Records     : {non_empty}")
    print(f"Missing/Invalid   : {empty}")

# Main file 
from data_loader import read_csv
from data_cleaner import drop_missing, fill_missing
from data_analyzer import mean, median, mode, maximum, minimum
from data_visualizer import plot_histogram, plot_bar_chart
from data_report import data_summary

def main():
    filepath = "students.csv"
    data = read_csv(filepath)
    print(" Data Loaded Successfully!")
    
    # Clean data
    data = fill_missing(data, 'Marks', 50)
    data = drop_missing(data, 'Marks')

    # Report
    data_summary(data)

    # Analysis
    print("\n Statistical Analysis:")
    print("Mean Marks   :", mean(data, 'Marks'))
    print("Median Marks :", median(data, 'Marks'))
    print("Mode Marks   :", mode(data, 'Marks'))
    print("Highest Marks:", maximum(data, 'Marks'))
    print("Lowest Marks :", minimum(data, 'Marks'))

    # Visualization
    print("\nGenerating Charts...")
    plot_bar_chart(data)
    plot_histogram(data, 'Marks')


if __name__ == "__main__":
    main()
    
