#Cafe Management system

#Define menu of Restaurant

menu = {
    'pizza':100,
    'pasta':80,
    "Burger":60,
    'salad':50,
    'Coffee':30,
}

#Greet a customer
print("Hello!!, Welcome to our Cafe!")
print("What do you want to order?")

#Ordering 
order = print(f"This is our menu {menu}")
order_total = 0

item_1 = input("Enter the item you want to order...")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Sorry!please order something else which we can serve you")

#for another item order

another_order=input("Do you want to order another item? (Yes/No)")
if another_order == "Yes":
    print("What would you like to order...")
    item_2 =  input("Enter the another item you want to order")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item has been added to your order..")
    else:
        print("Your ordered itrm {item_2} not available")

print(f"The Total Amount of your Order is {order_total}")
print("Thank You!!")





