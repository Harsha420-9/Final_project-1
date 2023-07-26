class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class RestaurantApp:
    def __init__(self):
        self.food_items = {}
        self.users = {}
        self.orders = []
        self.current_user = None

        # Adding Veg Food Items
        self.add_food_item("Veg Burger", "1 Piece", 150, 10, 50)
        self.add_food_item("Veg Pizza", "Medium", 300, 15, 30)
        self.add_food_item("Veg Biryani", "Full Plate", 200, 10, 40)

        # Adding Non-Veg Food Items
        self.add_food_item("Chicken Burger", "1 Piece", 180, 5, 40)
        self.add_food_item("Chicken Wings", "6 Pieces", 250, 10, 30)
        self.add_food_item("Mutton Curry", "Full Plate", 350, 0, 20)

    def admin_login(self):
        # Assume admin credentials are hardcoded for simplicity.
        admin_username = "admin"
        admin_password = "admin@123"
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        return True
        # if username == admin_username and password == admin_password:
        #     return True
        # else:
        #     print("Invalid admin credentials.")
        #     return False

    def user_registration(self):
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")

        user = User(full_name, phone_number, email, address, password)
        self.users[email] = user
        print("Registration successful!")

    def user_login(self):
        email = input("Email: ")
        password = input("Password: ")

        if email in self.users and self.users[email].password == password:
            self.current_user = self.users[email]
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items[food_id] = food_item
        # print(f"Food item '{name}' added successfully.")

    def edit_food_item(self):
        food_id = int(input("Enter FoodID to edit: "))

        if food_id in self.food_items:
            food_item = self.food_items[food_id]
            name = input("Enter Food Name: ")
            quantity = input("Enter Quantity: ")
            price = float(input("Enter Price (INR): "))
            discount = float(input("Enter Discount (%): "))
            stock = int(input("Enter Stock: "))

            food_item.name = name
            food_item.quantity = quantity
            food_item.price = price
            food_item.discount = discount
            food_item.stock = stock
            print("Food item updated successfully.")
        else:
            print("FoodID not found.")

    def view_food_items(self):
        print("FoodID\tName\t\tQuantity\tPrice\tDiscount\tStock")
        for food_id, food_item in self.food_items.items():
            print(
                f"{food_id}\t{food_item.name}\t{food_item.quantity}\t\t{food_item.price}\t{food_item.discount}%\t\t{food_item.stock}"
            )

    def remove_food_item(self):
        food_id = int(input("Enter FoodID to remove: "))

        if food_id in self.food_items:
            del self.food_items[food_id]
            print("Food item removed successfully.")
        else:
            print("FoodID not found.")

    def place_order(self):
        print("Available Food Items:")
        self.view_food_items()
        selected_items = input("Enter the FoodIDs separated by commas: ").split(",")
        selected_items = [int(item) for item in selected_items if item.isdigit()]

        order_items = []
        total_amount = 0

        for item_id in selected_items:
            if item_id in self.food_items:
                food_item = self.food_items[item_id]
                order_items.append(food_item)
                total_amount += food_item.price - (food_item.price * food_item.discount / 100)

        print("Selected Food Items:")
        for item in order_items:
            print(f"{item.name} ({item.quantity}) [INR {item.price}]")

        confirm_order = input("Place order? (yes/no): ").lower()
        if confirm_order == "yes":
            self.orders.append((self.current_user.email, order_items, total_amount))
            print("Order placed successfully!")
        else:
            print("Order canceled.")

    def view_order_history(self):
        print("Order History:")
        for email, order_items, total_amount in self.orders:
            print(f"User: {email}")
            print("Items:")
            for item in order_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print(f"Total Amount: INR {total_amount}")
            print("-" * 40)

    def update_profile(self):
        print("Update Profile:")
        if self.current_user:
            print("Current Profile:")
            print("Full Name:", self.current_user.full_name)
            print("Phone Number:", self.current_user.phone_number)
            print("Email:", self.current_user.email)
            print("Address:", self.current_user.address)
            print("Password:", self.current_user.password)

            self.current_user.full_name = input("Enter Full Name: ")
            self.current_user.phone_number = input("Enter Phone Number: ")
            self.current_user.address = input("Enter Address: ")
            self.current_user.password = input("Enter New Password: ")

            print("Profile updated successfully.")
        else:
            print("Please log in to update the profile.")

    def main(self):
        print("Welcome to Restaurant App!")
        while True:
            print("=" * 30)
            print("1. Admin Login")
            print("2. User Registration")
            print("3. User Login")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if self.admin_login():
                    while True:
                        print("=" * 30)
                        print("Admin Panel")
                        print("1. Add Food Item")
                        print("2. Edit Food Item")
                        print("3. View Food Items")
                        print("4. Remove Food Item")
                        print("5. Log Out")
                        admin_choice = int(input("Enter your choice: "))

                        if admin_choice == 1:
                            self.add_food_item(
                                input("Enter Food Name: "),
                                input("Enter Quantity: "),
                                float(input("Enter Price (INR): ")),
                                float(input("Enter Discount (%): ")),
                                int(input("Enter Stock: ")),
                            )
                        elif admin_choice == 2:
                            self.edit_food_item()
                        elif admin_choice == 3:
                            self.view_food_items()
                        elif admin_choice == 4:
                            self.remove_food_item()
                        elif admin_choice == 5:
                            print("Admin logged out.")
                            break
                        else:
                            print("Invalid choice.")

            elif choice == 2:
                self.user_registration()
            elif choice == 3:
                if self.user_login():
                    while True:
                        print("=" * 30)
                        print("User Panel")
                        print("1. Place New Order")
                        print("2. Order History")
                        print("3. Update Profile")
                        print("4. Log Out")
                        user_choice = int(input("Enter your choice: "))

                        if user_choice == 1:
                            self.place_order()
                        elif user_choice == 2:
                            self.view_order_history()
                        elif user_choice == 3:
                            self.update_profile()
                        elif user_choice == 4:
                            print("User logged out.")
                            break
                        else:
                            print("Invalid choice.")
            elif choice == 4:
                print("Thank you for using the Restaurant App!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = RestaurantApp()
    app.main()
