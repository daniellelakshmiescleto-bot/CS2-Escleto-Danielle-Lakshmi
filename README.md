# Movie Ticket Calculator

## Description
This program calculates the total cost for movie tickets based on customer choice and quantity, complete with input validation, error handling, and re-entry loops.

## Version 2 - Code with Input Validation and Re-entry
- Input: Accepts a customer's name, movie selection code, and ticket quantity with strict error-checking using `while` loops and `try-except` blocks.
- Process: Validates that the customer name is not empty, the movie choice is valid (1–3), and the ticket count is a positive integer, re-prompting the user until valid inputs are provided. Then calculates total cost using `total_cost = tickets * TICKET_PRICE`.
- Output: Validated customer name, selected movie title, and total cost in PHP (rounded to 2 decimal places).
- Validation Rules Implemented:
  - Customer name -- Must not be empty
  - Movie choice -- Must be a valid option (1, 2, or 3)
  - Tickets -- Positive whole number
