import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialize lists
ingredients = []
quantities = []
prices = []

print("=== Recipe Ingredient Cost Calculator ===")
print("Enter recipe ingredients. Type 'done' to finish.\n")

# User input loop
while True:
    name = input("Enter ingredient name: ").strip()
    if name.lower() == 'done':
        break
    try:
        quantity = float(input(f"Enter quantity of {name} (in grams or units): "))
        unit_price = float(input(f"Enter unit price of {name} (price per gram/unit in ₹): "))
        if quantity <= 0 or unit_price <= 0:
            print("Values must be greater than zero. Try again.\n")
            continue
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
        continue

    ingredients.append(name)
    quantities.append(quantity)
    prices.append(unit_price)
    print()

# Exit if no data
if not ingredients:
    print("\nNo ingredients entered. Exiting.")
else:
    # Create DataFrame
    df = pd.DataFrame({
        'Ingredient': ingredients,
        'Quantity': quantities,
        'Unit Price (₹)': prices
    })

    # Calculate cost
    df['Cost (₹)'] = np.round(df['Quantity'] * df['Unit Price (₹)'], 2)
    total_cost = df['Cost (₹)'].sum()

    # Display table
    print("\n=== Ingredient Cost Summary ===\n")
    print(df.to_string(index=False))
    print(f"\nTotal Recipe Cost: ₹{total_cost:.2f}")

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Ingredient'], df['Cost (₹)'], color='skyblue', edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.05, f'₹{height:.2f}', ha='center', fontsize=10)

    plt.title("Cost Breakdown per Ingredient", fontsize=14)
    plt.xlabel("Ingredient")
    plt.ylabel("Cost (₹)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
