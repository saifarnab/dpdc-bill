from datetime import datetime


def calculate_bill_with_breakdown(units, demand_charge, tax_percentage):
    # Define slab rates and their limits
    slabs = [
        (75, 5.26),
        (125, 7.20),
        (100, 7.59),
        (100, 8.02),
        (100, 12.67),
        (float('inf'), 14.61)  # last slab for units above 500
    ]

    remaining_units = units
    breakdown = []
    bill = 0

    for slab_limit, rate in slabs:
        if remaining_units <= 0:
            break

        # Units to charge in this slab
        slab_units = min(remaining_units, slab_limit)
        slab_amount = slab_units * rate

        breakdown.append({
            "units": slab_units,
            "rate": rate,
            "amount": round(slab_amount, 2)
        })

        bill += slab_amount
        remaining_units -= slab_units

    # Add demand charge and tax
    total_amount = bill + demand_charge
    tax_amount = total_amount * tax_percentage / 100
    total_amount += tax_amount

    return round(total_amount, 2), breakdown, round(tax_amount, 2)


# Main program
current_month_year = datetime.now().strftime("%B %Y")

curr_units = int(input("Current electricity units: "))
pre_units = int(input("Previous electricity units: "))
used_units = curr_units - pre_units

demand_charge = 252.0
tax_percentage = 5.0

bill_amount, breakdown, tax_amount = calculate_bill_with_breakdown(used_units, demand_charge, tax_percentage)

print('--------------------------------------')
print(f"Electricity Bill for {current_month_year}")
print(f"Units Consumed: {used_units} units\n")

print("Slab-wise Breakdown:")
for i, slab in enumerate(breakdown, start=1):
    print(f"  Slab {i}: {slab['units']} units × {slab['rate']} = {slab['amount']} taka")

print(f"\nDemand Charge: {demand_charge} taka")
print(f"Tax (@{tax_percentage}%): {tax_amount} taka")
print("--------------------------------------")
print(f"Total Payable: {bill_amount} taka")
