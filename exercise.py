"""
    Function to return the total cost of renting books
    Arguments:
    customer_name -- name of the customer renting books
    total_cost -- total cost to be paid
    cost_per_Day --cost of renting a book per day
    no_of_books_rented --total number of books rented
    no_of_days_rented --total days the book is rented
"""
import sys

def total_rental_cost():
    customer_name= input ("Enter your names ")
    cust_id = input ( "Enter your library customer ID")
    no_of_days_rented = input ("enter the total number of days the book was rented")
    cost_per_Day = 1
    total_cost = no_of_days_rented * no_of_books_rented
    
    return cust_name, total_cost