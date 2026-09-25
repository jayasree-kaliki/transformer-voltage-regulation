# Python Program to Calculate Voltage Regulation of a Transformer

import math

print("========================================")
print("   TRANSFORMER VOLTAGE REGULATION")
print("========================================")

# Input values
V2 = float(input("Enter secondary no-load voltage (V): "))
V2_fl = float(input("Enter secondary full-load voltage (V): "))

# Calculate voltage regulation
voltage_regulation = ((V2 - V2_fl) / V2_fl) * 100

# Display result
print("\n------------- RESULT ----------------")
print(f"No-load secondary voltage : {V2:.2f} V")
print(f"Full-load secondary voltage: {V2_fl:.2f} V")
print(f"Voltage Regulation         : {voltage_regulation:.2f} %")
print("-------------------------------------")
