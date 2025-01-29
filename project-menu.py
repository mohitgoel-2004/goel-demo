menu = {
   'Pizza':40,
   'Pasta':100,
   'Coffee':180,
   'Burger':60,
   'Salad':70,
}
print("welcome to goel restaurant")
print("Pizza : Rs40\nPasta: Rs100\nCoffee: Rs180\nBurger: Rs60\nSalad: Rs70")

Order_total = 0
item1 =input("Enter the name of item you want to order = ")
if item1 in menu:
    Order_total += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == 'Yes':
    item2 = input("Enter the name of second item =")
    if item2 in menu:
      Order_total += menu[item2]
      print(f"Your item {item2} has been added to your order")
    else:
      print(f"Ordered item {item2} is not available yet!")
      
print(f"The total amount of item to pay is {Order_total}")
    