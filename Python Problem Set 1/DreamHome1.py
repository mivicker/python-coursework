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

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)

monthly_salary = annual_salary/12

current_savings = 0
months = 0

while current_savings < (total_cost * 0.25):
    current_savings = current_savings * (1 + (.04)/12) + (monthly_salary * portion_saved)
    months += 1
    
print("Number of months to save:" + str(months))
