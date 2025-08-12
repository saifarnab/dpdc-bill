# Dhaka Power Distribution Company Limited (DPDC) Electricity Bill Calculator

A Python script to calculate electricity bills based on unit consumption, slab rates, demand charge, and tax percentage.  
It also provides a detailed slab-wise breakdown showing the number of units consumed in each slab and the corresponding amount charged.

---

## Features

- Calculates total electricity bill with slab-based rates.
- Includes demand charge and tax percentage.
- Provides slab-wise breakdown with units, rate, and amount.
- Easy to customize slab rates, demand charge, and tax percentage.

---

## Slab Rates

| Slab Range (Units) | Rate (Taka per Unit) |
|--------------------|----------------------|
| First 75           | 5.26                 |
| Next 125           | 7.20                 |
| Next 100           | 7.59                 |
| Next 100           | 8.02                 |
| Next 100           | 12.67                |
| Above 500          | 14.61                |

---

## Example Usage

```bash
$ python3 bill_calculator.py
Current electricity units: 650
Previous electricity units: 500
--------------------------------------
Electricity Bill for August 2025
Units Consumed: 150 units

Slab-wise Breakdown:
  Slab 1: 75 units × 5.26 = 394.5 taka
  Slab 2: 75 units × 7.2 = 540.0 taka

Demand Charge: 252.0 taka
Tax (@5.0%): 59.34 taka
--------------------------------------
Total Payable: 1245.84 taka
