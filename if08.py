def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number == 1:
        hafta = "Monday"

    elif number == 2:
        hafta = "Tuesday"

    elif number == 3:
        hafta = "Wednesday"

    elif number == 4:
        hafta = "Thursday"

    elif number == 5:
        hafta = "Friday"

    elif number == 6:
        hafta = "Saturday"

    elif number == 7:
        hafta = "Sunday"

    return hafta

print(main(3))