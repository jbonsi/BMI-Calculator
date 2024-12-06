def calculate_bmi(weight_lbs: float, height_ft: int, height_in: float) -> float:
    """calculates BMI using weight in pounds and height in feet and inches for accuracy"""
    total_height_in = (height_ft * 12) + height_in
    bmi = (weight_lbs / (total_height_in ** 2)) * 703
    return round(bmi, 1)

def classify_bmi(bmi: float) -> str:
    """classifies BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the Body Mass Index Calculator!")
    weight = float(input("Enter your weight in pounds: "))
    height_ft = int(input("Enter your height (feet): "))
    height_in = float(input("Enter additional height (inches, can be decimal): "))

    bmi = calculate_bmi(weight, height_ft, height_in)
    classification = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Classification: {classification}")

if __name__ == "__main__":
    main()
