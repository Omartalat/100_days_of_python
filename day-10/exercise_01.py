def is_leap(year):
    """
    is_leap return True if this year is a leap year; Otherwise return False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    return # of days in the given month
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not year or not month:
        return
    if month == 2 and is_leap(year):
        return 29
    else:
        month -= 1
        days = month_days[month]
        return days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
