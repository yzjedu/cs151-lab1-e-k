# Programmers: Krishon Pinkins and Eric Thomas
# Course: CS151, Professor Zee
# Due Date: 9/17/2024
# Lab Assignment: 1
# Problem Statement: The program collects the mpg, cost of gas per gallon, and number of miles in a trip/
# to generate a trip cost
#Data In: Code needs input of mpg, miles, and cost of gas per gallon
#Data Out: Code prints output of trip cost

# Code should ask users to input their mpg, cost of gas per gallon, and miles
print('How much is your miles per gallon?')
miles_per_gallon = int(input())
print('How much is your cost of gas per gallon?')
gas_per_gallon = int(input())
print('How many miles are you commuting?')
miles = int(input())
# Code should use users input to calculate the cost of the trip and print it to the user
trip_cost = (miles / miles_per_gallon) * gas_per_gallon#(float(miles)/float(miles_per_gallon)) * float(gas_per_gallon)
print('Your trip cost is $'+str(trip_cost))