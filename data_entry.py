from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I" : "Income" , "E" : "Expenses"}
def get_date(prompt , allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str : 
        return datetime.today().strftime(date_format)
    
    try :
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print(f" Invalid date format . You have to add date in this fromat : {date_format} .")
        return get_date(prompt , allow_default)


def get_amount():
    try :
        amount = float(input("Enter te amount :"))
        if (amount <= 0):
            raise ValueError("Amount provides must be postive , and non-zero value .")
        return amount
    except ValueError as e :
        print(e)
        get_amount()

def get_category():
    category= input("Enter the category ('I' for Income or 'E' for Expenses) :").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print(f"Invalid category . Please enter ('I' for Income or 'E' for Expenses) .")
    return get_category

def get_description():
    return input("Enter a description (optional) :")


# date = get_date("Enter the date: ", allow_default=True)
# print(f"The date entered is: {date}")
# amount = get_amount()
# print(f"The amount entered is: {amount}")
# category = get_category()
# print(f"The catergory you entered is : {category}")