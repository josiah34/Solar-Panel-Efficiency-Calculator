import csv
from datetime import date


def export_to_csv(panel_efficiency, area, panel_power):
    today = date.today().strftime("%Y-%m-%d")
    try:
        with open("efficiency.csv", "a", newline="") as f:
            writer = csv.writer(f)
            # Check if the file is empty and write the header row if needed
            if f.tell() == 0:
                writer.writerow(
                    [
                        "Panel Efficiency (%)",
                        "Area (sq. meters)",
                        "Panel Power (W)",
                        "Date",
                    ]
                )
            writer.writerow([panel_efficiency, area, panel_power, today])
        print("File exported successfully!")
    except IOError:
        print("An error occurred while exporting the file.")


# Function to get user input and validate it
def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_efficiency(panel_power, area):
    SUNLIGHT_POWER = 1000
    panel_efficiency = (panel_power / (area * SUNLIGHT_POWER)) * 100
    panel_efficiency = round(panel_efficiency, 2)
    choice = input("Would you like to export the efficiency result to a CSV? y or n: ")
    if choice.lower() == "y":
        export_to_csv(panel_efficiency, area, panel_power)
    elif choice.lower() == "n":
        print("Result not exported.")
    return panel_efficiency


def main():
    while True:
        area = get_user_input(
            "Enter the area of the solar panel in square meters(m^2): "
        )
        panel_power = get_user_input("Enter the power of the solar panel in watts(W): ")
        print(calculate_efficiency(panel_power, area))

        choice = input("Press 'y' to continue or 'n' to stop: ")
        if choice.lower() == "y":
            print("Continuing...")
        elif choice.lower() == "n":
            print("Stopping...")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
