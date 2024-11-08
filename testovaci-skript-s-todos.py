import datetime

def get_current_date():
    """Returns the current date in YYYY-MM-DD format"""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def greet_user(username):
    """Greets the user"""
    # TODO: Add a personalized greeting based on the time of day (e.g., good morning, good afternoon, good evening)
    print(f"Hello, {username}! Today is {get_current_date()}.")

def calculate_age(year_of_birth):
    """Calculates the user's age based on their birth year"""
    current_year = datetime.datetime.now().year
    age = current_year - year_of_birth
    # FIXME: Verify that the age is correct for someone born this year who hasn’t had their birthday yet
    return age

def display_user_info(username, year_of_birth):
    """Displays user information"""
    greet_user(username)
    age = calculate_age(year_of_birth)
    print(f"{username} is {age} years old.")

# Main program function
def main():
    username = "Pepa"
    year_of_birth = 2000

    # TODO: Add user input for entering their name and year of birth
    display_user_info(username, year_of_birth)

    # FIXME: If the user enters an invalid year, display an error message
    # TODO: Implement input validation

if __name__ == "__main__":
    main()
