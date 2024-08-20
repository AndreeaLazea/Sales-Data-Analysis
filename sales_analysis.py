"""
sales_analysis.py

A simple Python script that performs data analysis on sales data.

Features:
- Reads sales data from a CSV file.
- Calculates total units sold per product.
- Computes average revenue per unit for each product.
- Identifies the day with the highest total revenue.
- Outputs a summary to a text file.

Usage:
Ensure 'sales_data.csv' is in the same directory as this script.
Run the script with Python 3: `python sales_analysis.py`
"""

import csv
import numpy as np
import pandas as pd


def calculate_total_units_sold(sales_data):
    """
    Calculates the total units sold for each prodcut
    :param sales_data : (DataFrame) the sales data as pandas DataFrame
    :return: Total units sold for each product
    """

    total_units_sold = sales_data.groupby("Product")['Units Sold'].sum()
    return total_units_sold


def calculate_total_profit_sold(sales_data):
    """
    Calculates the total profit sold
    :param sales_data : (DataFrame) the sales data as pandas DataFrame
    :return: returns the total profit for each product
    """
    total_profit_sold = sales_data.groupby("Product")["Total Revenue"].sum()
    return total_profit_sold


def calculate_highest_revenue_day(sales_data):
    """
    Calculates the day with the biggest revenue
    :param sales_data: (DataFrame) the sales data as pandas DataFrame
    :return: returns the highest revenue day with all its components
    """
    highest_revenue = sales_data.loc[sales_data["Total Revenue"].idxmax()]
    return highest_revenue


def calculate_revenue_sum(revenue_array):
    """
    Calculates the revenue sum for all products
    :param revenue_array: array of all revenues as numpy array
    :return:  returns the sum of the revenue for all products
    """
    total_revenue = np.sum(revenue_array)
    return total_revenue


def calculate_mean_revenue(revenue_array):
    """
    Calculates the mean of the revenues
    :param revenue_array: array of all revenues as numpy array
    :return: returns the mean of the revenue for all products
    """
    mean_revenue = np.mean(revenue_array)
    return mean_revenue


def calculate_median_revenue(revenue_array):
    """
    Calculates the median of the revenues
    :param revenue_array: array of all revenues as numpy array
    :return: returns the median of the revenue for all products
    """
    median_revenue = np.median(revenue_array)
    return median_revenue


def write_summary_to_file(output_file, total_units_sold, total_profit_sold, highest_revenue_day, revenue_sum,
                          mean_revenue, median_revenue):
    # output_file = "sales_summary.txt"

    try:
        with open(output_file, 'w') as f:
            f.write("Sales Data Analysis Summary \n")
            f.write("===========================\n\n")
            f.write(f"====Total profit: ${revenue_sum:.2f}\n")
            f.write(f"====Median Revenue: ${median_revenue:.2f}\n")
            f.write(f"====Mean Revenue: ${mean_revenue:.2f}\n")
            f.write(f"====Total units sold: \n")
            f.write(total_units_sold.to_string() + "\n")
            f.write(f"====Total profit: \n")
            f.write(total_profit_sold.to_string() + "\n")
            f.write(f"====The Highest Revenue: \n")
            f.write(highest_revenue_day.to_string() + "\n")
    except Exception as e:
        print("There was an error: ", e)


def main():
    file_path = "sales_data.csv"
    sales_data = pd.read_csv(file_path)
    print("Data: \n", sales_data)
    output_file = "sales_summary.txt"
    revenue_array = np.array(sales_data["Total Revenue"])
    total_units_sold = calculate_total_units_sold(sales_data)
    total_profit_sold = calculate_total_profit_sold(sales_data)
    highest_revenue_day = calculate_highest_revenue_day(sales_data)
    revenue_sum = calculate_revenue_sum(revenue_array)
    mean_revenue = calculate_mean_revenue(revenue_array)
    median_revenue = calculate_median_revenue(revenue_array)
    write_summary_to_file(output_file, total_units_sold, total_profit_sold, highest_revenue_day, revenue_sum,
                          mean_revenue, median_revenue)


if __name__ == "__main__":
    main()
