# -*- coding: utf-8 -*-

"""
You have got out of your dead end career and you're trying to save to build a blocky monstrosty to live in.
You're going to need a lot of money to pay a shit eating architect.

This program asks you how many months it will take before you have a down payment ready for your home,
so you can decide if this whole thing is worth it or if you're going to be living downstairs from some
useless rich children for your whole life.
"""


annual_salary = input("Please enter your yearly human worth to global capitalism:")

annual_salary = float(annual_salary)


def calculate_savings_at_rate(rate, annual_salary, months, semi_annual_raise):
    """    
    This function will calculate your savings at a given rate.
    
    Inputs: rate: Savings Rate
            salary: Annual Salary
            months: Months in which you hope to meet your goal.
    
    Outputs:current_savings: Your total savings at the end of your goal period.
    """
    current_savings = 0 
    monthly_salary = annual_salary/12
    
    for i in range(months):
        current_savings = current_savings * (1 + (.04)/12) + (monthly_salary * rate)
            
        if i % 6 == 0:
            annual_salary = annual_salary + annual_salary * semi_annual_raise
            monthly_salary = annual_salary/12
                
    return current_savings

epsilon = 100
num_guesses = 0
low = 0
high = 10000

rate = high/10000
ans = calculate_savings_at_rate(rate, annual_salary, 36, 0.07)
distance_from_goal = abs(ans - (250000))

if ans < (250000):
    print("Your are unable to save enough in the given time.")
    
else:
    while distance_from_goal > 100:
        split = (low + high)//2
        rate = split/10000
        ans = calculate_savings_at_rate(rate, annual_salary, 36, 0.07)
        distance_from_goal = abs(ans - (250000))
        
        print("Low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
        num_guesses += 1
        
        if ans < (250000):
            low = rate
        else:
            high = rate
        
    print("Number of guesses: " + str(num_guesses))
    print("Savings rate: " + str(rate))
        
            