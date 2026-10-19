# Travel Fare Calculator

## Description
This program calculates the total travel fare based on distance, number of passengers, and a fixed rate per kilometer.

## Version 1 - Original code without input validation
- Input: Accepts a passenger's name, distance in kilometers, and number of passengers.
- Process: Calculates the total fare using `total_fare = distance * FARE_RATE * passengers`.
- Output: Passenger name and total fare in PHP (rounded to 2 decimal places).
- Validation Rules:
  - Passenger name -- Must not be empty
  - Distance -- Number greater than 0
  - Passengers -- Positive whole number
- Does not include input validation in code execution.
