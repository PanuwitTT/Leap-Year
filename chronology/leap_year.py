"""Leap Year utility."""
#Standard Library 

#3rd Party Library

#Project Library

#_______________________________________________________
def is_leap_year(year: int) -> bool:
    """Determine if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
