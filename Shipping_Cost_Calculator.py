# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter package weight in kilograms: "))
rate = float(input("Enter package rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display result
print(f"Shipping Cost: {shipping_cost} USD")
