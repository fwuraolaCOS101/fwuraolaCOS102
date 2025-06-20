# Project II

def calculate_atr(years_of_experience, age):
    if years_of_experience > 25 and age >= 55:
        return 5600000
    elif years_of_experience > 20 and age >= 45:
        return 4480000
    elif years_of_experience > 10 and age >= 35:
        return 1500000
    elif years_of_experience < 10 and age < 35:
        return 550000
    else:
        return 0  # If none of the conditions match

# Example usage
experience = int(input("Enter years of experience: "))
age = int(input("Enter age: "))
atr = calculate_atr(experience, age)

if atr == 0:
    print("No ATR assigned based on given criteria.")
else:
    print(f"The Annual Tax Revenue (ATR) is ₦{atr:,}")