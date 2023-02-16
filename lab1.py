def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = int(input("Enter the current year: "))
        age = current_year - birth_year
        print("Your age is:", age)
    except TypeError:
        print("Please enter an int")

def hello_world():
    print("Hello World")

calculate_age()
hello_world()
