# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:28:24 2019

@author: vicke
"""

annual_salary = input("Please enter your yearly human worth to global capitalism:")
total_cost = input("Please enter the cost of your desired property:")
semi_annual_raise = input("How much more can you squeeze out of them?")
months = input("What is your time frame?")

annual_salary = float(annual_salary)
total_cost = float(total_cost)
semi_annual_raise = float(semi_annual_raise)
months = int(months)

def calculate_savings(save_percent, annual_salary, months):
    current_savings = 0
    monthly_salary = annual_salary/12
    for month in range(months):
        current_savings = current_savings * (1 + (.04)/12) + (monthly_salary * save_percent)
        
        if month % 6 == 0:
            annual_salary = annual_salary + annual_salary * semi_annual_raise
            monthly_salary = annual_salary/12
    
    return current_savings

savings_goal = (0.25 * total_cost)
epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess_percent = 10000
current_savings = calculate_savings(guess_percent/10000, annual_salary, months)
if current_savings < savings_goal:
    print("You are unable to buy this property on the given time frame.")
    
else:
    guess_percent = (high + low)//2
    current_savings = calculate_savings(guess_percent/10000, annual_salary, months)
    while abs(current_savings - savings_goal) >= epsilon:
        if current_savings < savings_goal:
            low = guess_percent
        else:
            high = guess_percent
            
        guess_percent = (high + low)//2
        current_savings = calculate_savings(guess_percent/10000, annual_salary, months)
        num_guesses += 1
        print("Number of Guesses: " + str(num_guesses) + " Savings_rate: " + str(guess_percent/10000))