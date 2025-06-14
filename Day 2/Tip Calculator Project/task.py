#task

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")


# Extra Credit

# Water intake Calculator

weight = (float(input("\nHow much do you weigh in pounds? ")))
exercise_minutes = (float(input("\nHow many minutes do you exercise? ")))

print(weight)
print(exercise_minutes)


base_water = (weight * 0.5) + 12 * (45 / 30)

print(base_water)

print(f"You should intake about {base_water} ounces of water every day!")



