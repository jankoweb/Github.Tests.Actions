import datetime

def get_current_date():
    """Vrátí aktuální datum ve formátu YYYY-MM-DD"""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def greet_user(username):
    """Pozdrav uživatele"""
    # TODO: Přidat personalizovaný pozdrav podle denní doby (např. dobré ráno, dobré odpoledne, dobrý večer)
    print(f"Ahoj, {username}! Dnes je {get_current_date()}.")

def calculate_age(year_of_birth):
    """Spočítá věk uživatele na základě roku narození"""
    current_year = datetime.datetime.now().year
    age = current_year - year_of_birth
    # FIXME: Ověřit, jestli je věk správný pro někoho, kdo se narodil ještě letos a neměl narozeniny
    return age

def display_user_info(username, year_of_birth):
    """Zobrazí informace o uživateli"""
    greet_user(username)
    age = calculate_age(year_of_birth)
    print(f"{username} má {age} let.")

# Hlavní funkce programu
def main():
    username = "Pepa"
    year_of_birth = 2000

    # TODO: Přidat vstup pro uživatele, aby zadal své jméno a rok narození
    display_user_info(username, year_of_birth)

    # FIXME: Pokud uživatel zadá neplatný rok, zobrazit chybovou zprávu
    # TODO: Implementovat kontrolu platnosti vstupu

if __name__ == "__main__":
    main()
