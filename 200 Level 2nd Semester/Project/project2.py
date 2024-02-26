def calculate_bill(previous_reading, current_reading, cost_per_unit, vat_rate):
    unit_diff = current_reading - previous_reading
    total_cost = unit_diff * cost_per_unit
    vat_amount = total_cost * (vat_rate / 100)
    final_cost = total_cost + vat_amount
    return final_cost


# Input
name = input("Enter customer name: ")
address = input("Enter customer address: ")
meter_number = input("Enter meter number: ")
previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))
cost_per_unit = float(input("Enter cost per unit: "))
vat_rate = float(input("Enter VAT rate (%): "))
bill_amount = calculate_bill(previous_reading, current_reading, cost_per_unit, vat_rate)

print("\nCustomer Details:")
print("Name:", name)
print("Address:", address)
print("Meter Number:", meter_number)
print("\nPower Consumption Details:")
print("Previous Reading:", previous_reading)
print("Current Reading:", current_reading)
print("Unit Difference:", current_reading - previous_reading)
print("\nBilling Details:")
print("Cost per Unit:", cost_per_unit)
print("VAT Rate:", vat_rate, "%")
print("Total Cost:", bill_amount)
