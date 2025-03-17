def calculate_bmi(weight: float, height: float):
    """
    Calculate BMI given weight (kg) and height (cm).
    
    Args:
    weight (float): Weight in kilograms
    height (float): Height in cm
    
    Returns:
    float: BMI value
    """
    if height <= 0 or weight <= 0:
        raise ValueError("values should be positive")
    
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def gender_to_number(gender: str) -> int:
    if gender == "M":
        return 0
    if gender == "F":
        return 1
    raise ValueError(f"unknown gender: {gender}")

def long_event_to_short(gender: bool, sport: str, event: str) -> str:
    if not event.startswith(sport):
        raise ValueError("unknown event")
    event = event.removeprefix(sport)
    event = event.lstrip()
    return event
    string_gender = "Women's" if gender else "Men's"
    if not event.startswith(string_gender):
        raise ValueError(f"unknown event gender: {event}, {sport}")
    
    event = event.removeprefix(string_gender)
    return event.lstrip()

if __name__ == "__main__":
    # Example usage
    weight = 70  # kg
    height = 175  # cm
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi}")
