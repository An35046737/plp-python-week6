# Week 6 Assignment - Safe Error Handling

This project demonstrates how to use `try` and `except` in Python to handle errors safely without crashing the program.

## Files

* `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary field lookup.
* `unbreakable.py` - Demonstrates how to safely handle invalid user input.
* `README.md` - Describes the assignment and the purpose of each file.

## Why can the `if` check not catch `abc` on its own?

An `if` check cannot directly catch `"abc"` when converting it to an integer because `int("abc")` raises a `ValueError`. The `try`/`except` block catches this error and allows the program to continue running instead of crashing.
