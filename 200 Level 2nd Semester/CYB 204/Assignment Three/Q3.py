def calculate_total_weight(widgets, gizmos):
    widget_weight = 75  # grams
    gizmo_weight = 112  # grams

    total_weight = (widgets * widget_weight) + (gizmos * gizmo_weight)

    # Display the total weight of the order
    print(f"Total Weight of the Order: {total_weight} grams")

# Get user input for the number of widgets and gizmos
widgets = int(input("Enter the number of widgets: "))
gizmos = int(input("Enter the number of gizmos: "))

# Calculate and display the total weight of the order
calculate_total_weight(widgets, gizmos)
