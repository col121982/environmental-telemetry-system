def calculate_current(voltage, resistance):
    current = voltage / resistance
    return current

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohms): "))

current = calculate_current(voltage, resistance)
current_ma = current * 1000

print("Current:", current, "A")
print("Current:", current_ma, "mA")