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

if __name__ == "__main__":
    # Example usage
    weight = 70  # kg
    height = 175  # cm
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi}")
