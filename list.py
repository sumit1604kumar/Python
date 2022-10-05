def days_of_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported units"


def validate(ab):
    #if user_input.isdigit():
    try:
        user_input_number = int(ab["day"])
        if user_input_number > 0 :
            calculated_value = days_of_units(user_input_number, ab["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, kindly enter positive number")
        else:
            print( "negative number, nothing for you")

    except ValueError:
        print("not a valid number")


user_input_message = "enter lucky number"