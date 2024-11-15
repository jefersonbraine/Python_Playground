import calendar

def display_calendar():

    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    cal = calendar.TextCalendar(calendar.SUNDAY)

    mont_calendar = cal.formatmonth(year, month)
    print(mont_calendar)

display_calendar()