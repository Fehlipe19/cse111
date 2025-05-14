#To enhance my program, I added a feature that show the user hwo much the tire costs, and a feature that allows the user to input their phone number if they decide to buy the tire.

import math
from datetime import datetime

# Tire Volume Calculator

width_mm = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter_inches = float(input("Enter the diameter of the tire in inches: "))

tire_volume_liters = math.pi * width_mm ** 2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inches) / 10000000000

print(f"\nThe volume of the tire is approximately {tire_volume_liters:.2f} liters.\n")

full_date = datetime.now()
tire_price = 0

if width_mm < 205:
    tire_price = 89.99
elif 205 <= width_mm < 225:
    tire_price = 103.99
elif 225 <= width_mm < 245:
    tire_price = 119.99
elif width_mm >=245:
    tire_price = 145.99

will_buy = input(f"The price of the tire is ${tire_price:.2f}. Will you buy this tire? (yes/no): ").strip().lower()
if will_buy == "yes":
    customer_phone_number = input("Please enter your phone number: ")
    with open("volumes.txt", "a") as file:
        file.write(f"{full_date.strftime('%Y-%m-%d')}, {width_mm}, {aspect_ratio}, {diameter_inches}, {tire_volume_liters:.2f}, {customer_phone_number}\n")
    print(f"\nSale completed $$! Come back soon.\n")
else:
    with open("volumes.txt", "a") as file:
        file.write(f"{full_date.strftime('%Y-%m-%d')}, {width_mm}, {aspect_ratio}, {diameter_inches}, {tire_volume_liters:.2f}\n")  
    print("\nOk, maybe next time.\n")
                         


with open("volumes.txt", "r") as file:
    content = file.read()
    print(content)