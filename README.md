## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.


## Rationale
2.1 what refactoring signs (code smells) suggest this refactoring?
- Middle Man: The `Movie` class acts as a "middle man" between `Rental` and `Pricestrategy` by requiring Rental to 
call Movie to access pricing data.

2.2 what design principle suggests this refactoring? Why?
- Single Responsibility Principle: To separate responsibilities between the `Movie` class, which should focus only on 
movie data, and the `Rental` class, which should handle the rental process and pricing logic

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

