import datetime

print("=======================================")
print("   Welcome to the Daily Calorie Tracker")
print("=======================================")
print("This tool helps you log meals, calculate total calories,")
print("and compare your intake with your daily calorie limit.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)

# Task 3: Calorie Calculations
total_cal = sum(calories)
avg_cal = total_cal / len(calories)

limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_cal > limit:
    status = " You have exceeded your daily calorie limit!"
else:
    status = " You are within your daily calorie limit!"

# Task 5: Neatly Formatted Output
print("\n\n----------- Calorie Summary -----------")
print(f"{'Meal Name':<15}{'Calories'}")
print("---------------------------------------")

for meal, cal in zip(meals, calories):
    print(f"{meal:<15}{cal}")

print("---------------------------------------")
print(f"{'Total:':<15}{total_cal}")
print(f"{'Average:':<15}{avg_cal:.2f}")
print("---------------------------------------")
print(status)
print("---------------------------------------")

# Task 6: Bonus - Save Session Log
save = input("\nDo you want to save this session report? (yes/no): ").lower()

if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write("-----------------------------------\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        for meal, cal in zip(meals, calories):
            file.write(f"{meal:<15}{cal}\n")
        file.write("-----------------------------------\n")
        file.write(f"Total: {total_cal}\n")
        file.write(f"Average: {avg_cal:.2f}\n")
        file.write(status + "\n")
    print(f"\n Report saved successfully as '{filename}'.")

print("\nThank you for using the Daily Calorie Tracker!")