def calculate_admission_cost(ages):
    free_age_limit = 2
    child_age_limit = 12
    senior_age_limit = 65

    child_cost = 14.00
    senior_cost = 18.00
    other_cost = 23.00

    total_cost = 0.0

    for age in ages:
        if age == '':
            break  # Stop taking input if a blank line is entered
        age = int(age)
        if age <= free_age_limit:
            # Guests 2 years of age and less are admitted without charge
            continue
        elif 3 <= age <= child_age_limit:
            total_cost += child_cost
        elif age >= senior_age_limit:
            total_cost += senior_cost
        else:
            total_cost += other_cost

    # Display the admission cost for the group
    print(f"Admission Cost for the Group: ${total_cost:.2f}")

# Get user input for ages
ages = []
while True:
    age_input = input("Enter the age of a guest (press Enter for no more guests): ")
    if not age_input:
        break  # Break the loop if a blank line is entered
    ages.append(age_input)

# Calculate and display the admission cost
calculate_admission_cost(ages)
