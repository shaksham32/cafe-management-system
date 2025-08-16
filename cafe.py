menu = {
    1: ("Coffee", 50),
    2: ("Tea", 30),
    3: ("Sandwich", 100),
    4: ("Cake", 80)
}

def show_menu():
    print("Menu:")
    for num, (item, price) in menu.items():
        print(f"{num}. {item} - ₹{price}")

def take_order():
    order = {}
    while True:
        choice = int(input("Enter item number (0 to finish): "))
        if choice == 0:
            break
        if choice in menu:
            qty = int(input("Enter quantity: "))
            order[choice] = order.get(choice, 0) + qty
        else:
            print("Invalid choice, try again.")
    return order

def print_bill(order):
    print("\nYour Bill:")
    total = 0
    for item_no, qty in order.items():
        item, price = menu[item_no]
        cost = price * qty
        total += cost
        print(f"{item} x{qty} = ₹{cost}")
    print(f"Total = ₹{total}")

def main():
    print("Welcome to Simple Cafe!")
    show_menu()
    order = take_order()
    if order:
        print_bill(order)
    else:
        print("No order placed.")

if __name__ == "__main__":
    main()
