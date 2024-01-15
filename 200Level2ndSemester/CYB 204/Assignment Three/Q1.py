def calculate_bill(minutes_used, messages_used):
    base_charge = 15.00
    additional_minute_charge = 0.25
    additional_message_charge = 0.15
    emergency_charge = 0.44
    sales_tax_rate = 0.05

    # Calculate additional charges
    additional_minute_cost = max(0, minutes_used - 50) * additional_minute_charge
    additional_message_cost = max(0, messages_used - 50) * additional_message_charge

    # Calculate subtotal before tax
    subtotal = base_charge + additional_minute_cost + additional_message_cost + emergency_charge

    # Calculate tax
    sales_tax = subtotal * sales_tax_rate

    # Calculate total bill
    total_bill = subtotal + sales_tax

    # Print the results
    print(f"Base Charge: ${base_charge:.2f}")
    if additional_minute_cost > 0:
        print(f"Additional Minutes Charge: ${additional_minute_cost:.2f}")
    if additional_message_cost > 0:
        print(f"Additional Messages Charge: ${additional_message_cost:.2f}")
    print(f"911 Charge: ${emergency_charge:.2f}")
    print(f"Tax Amount: ${sales_tax:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")

# Get user input
minutes_used = int(input("Enter the number of minutes used: "))
messages_used = int(input("Enter the number of text messages used: "))

# Calculate and display the bill
calculate_bill(minutes_used, messages_used)
