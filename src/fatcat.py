"""Input salary and boolean bonus to determine a banker's year end take home.
If the banker gets a bonus, return his salary * 10. Otherwise return salary.
Return in $XX format."""


def bonus_time(salary, bonus):
    return "${}".format(salary * 10) if bonus else "${}".format(salary)
