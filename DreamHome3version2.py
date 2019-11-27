# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:28:24 2019

@author: vicke
"""

annual_salary = input("Please enter your yearly human worth to global capitalism:")
portion_saved = input("How much can you spare avoiding starvation?")
total_cost = input("Please enter the cost of your desired property:")
semi_annual_raise = input("How much more can you squeeze out of them?")

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)
semi_annual_raise = float(semi_annual_raise)

monthly_salary = annual_salary/12

current_savings = 0
months = 0

while current_savings < (total_cost * 0.25):
    current_savings = current_savings * (1 + (.04)/12) + (monthly_salary * portion_saved)
    months += 1
    
    if months % 6 == 0:
        annual_salary = annual_salary + annual_salary * semi_annual_raise
        monthly_salary = annual_salary/12
    
print("Number of months to save:" + str(months))