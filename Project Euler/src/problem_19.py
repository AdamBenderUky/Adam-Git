#problem_19.py

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def count_sundays_on_first():
    # Days in each month
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Start on 1 Jan 1901 which is a Tuesday
    day_of_week = 2  # 0: Sunday, 1: Monday, ..., 6: Saturday
    sundays_count = 0

    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:
                sundays_count += 1
            
            # Move to the first day of the next month
            if month == 1 and is_leap_year(year):
                day_of_week = (day_of_week + 29) % 7
            else:
                day_of_week = (day_of_week + months[month]) % 7

    return sundays_count

if __name__ == "__main__":
    result = count_sundays_on_first()
    print("Number of Sundays that fell on the first of the month during the twentieth century:", result)
