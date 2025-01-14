budget = 50
usb_price = 6

num_usb_sticks = budget // usb_price
remaining_money = budget % usb_price

print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{remaining_money} left.")
