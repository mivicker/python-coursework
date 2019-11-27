# -*- coding: utf-8 -*-

"""
You have got out of your dead end career and you're trying to save to build a blocky monstrosty to live in.
You're going to need a lot of money to pay a shit eating architect.

This program asks you how many months it will take before you have a down payment ready for your home,
so you can decide if this whole thing is worth it or if you're going to be living downstairs from some
useless rich children for your whole life.
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
