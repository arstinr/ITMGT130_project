class DeliveryManagementSystem:
    def __init__(self):
        self.orders = []
        self.customers = []
        self.delivery_staff = []
        # hardcode branches
        self.branches = {
            'Ortigas Avenue': {'id': 1, 'location': 'Ortigas'},
            'Shangri-La Plaza': {'id': 2, 'location': 'Shangri-La'},
            'Katipunan Avenue': {'id': 3, 'location': 'Katipunan'}
        }
        # hardcode menu items
        self.menu = {
            'Sushi': 200,
            'Ramen': 300,
            'Tempura': 250,
            'Teriyaki Chicken': 350,
            'Miso Soup': 100
        }

    def add_customer(self, name, address, contact):
        self.customers.append({
            'id': len(self.customers) + 1,
            'name': name,
            'address': address,
            'contact': contact
        })
        print(f"Customer '{name}' added successfully.")

    def add_delivery_staff(self, name, branch_name):
        branch = self.branches.get(branch_name)
        if branch:
            self.delivery_staff.append({
                'id': len(self.delivery_staff) + 1,
                'name': name,
                'branch_id': branch['id']
            })
            print(f"Delivery staff '{name}' added successfully to branch '{branch_name}'.")
        else:
            print(f"Branch '{branch_name}' does not exist.")

    def place_order(self, customer_id, branch_name, items):
        branch = self.branches.get(branch_name)
        if branch:
            order_items = []
            total_price = 0
            for item, quantity in items.items():
                if item in self.menu:
                    item_price = self.menu[item] * quantity
                    order_items.append({'item': item, 'quantity': quantity, 'price': item_price})
                    total_price += item_price
            self.orders.append({
                'id': len(self.orders) + 1,
                'customer_id': customer_id,
                'branch_id': branch['id'],
                'items': order_items,
                'total_price': total_price,
                'status': 'Pending'
            })
            print(f"Order placed successfully! Total price: {total_price}")
        else:
            print(f"Branch '{branch_name}' does not exist.")

    def assign_delivery(self, order_id, staff_id):
        for order in self.orders:
            if order['id'] == order_id:
                order['staff_id'] = staff_id
                order['status'] = 'Assigned'
                print(f"Order ID '{order_id}' assigned to staff ID '{staff_id}'.")
                break

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order['id'] == order_id:
                order['status'] = status
                print(f"Order ID '{order_id}' status updated to '{status}'.")
                print(f"Customer notified of new status: {status}")
                break

    def view_orders(self, branch_name):
        branch = self.branches.get(branch_name)
        if branch:
            return [order for order in self.orders if order['branch_id'] == branch['id']]
        else:
            print(f"Branch '{branch_name}' does not exist.")
            return []

def main():
    system = DeliveryManagementSystem()

    while True:
        print("\n1. Add Customer")
        print("2. Add Delivery Staff")
        print("3. Place Order")
        print("4. Assign Delivery")
        print("5. Update Order Status")
        print("6. View Orders")
        print("7. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            contact = input("Enter customer contact: ")
            system.add_customer(name, address, contact)

        elif choice == '2':
            name = input("Enter staff name: ")
            branch_name = input("Enter branch name (Ortigas Avenue, Shangri-La Plaza, Katipunan Avenue): ")
            system.add_delivery_staff(name, branch_name)

        elif choice == '3':
            customer_id = int(input("Enter customer ID: "))
            branch_name = input("Enter branch name (Ortigas Avenue, Shangri-La Plaza, Katipunan Avenue): ")
            items = {}
            while True:
                item = input("Enter item (Sushi: Php 200, Ramen: Php 300, Tempura: Php 250, Teriyaki Chicken: Php 350, Miso Soup: Php 100): ")
                if item not in system.menu:
                    print("Invalid item. Please try again.")
                    continue
                quantity = int(input(f"Enter quantity of {item}: "))
                items[item] = quantity
                more_items = input("Add another item? (y/n): ")
                if more_items.lower() != 'y':
                    break
            system.place_order(customer_id, branch_name, items)

        elif choice == '4':
            order_id = int(input("Enter order ID: "))
            staff_id = int(input("Enter staff ID: "))
            system.assign_delivery(order_id, staff_id)

        elif choice == '5':
            order_id = int(input("Enter order ID: "))
            status = input("Enter new status (e.g., Delivered): ")
            system.update_order_status(order_id, status)

        elif choice == '6':
            branch_name = input("Enter branch name (Ortigas Avenue, Shangri-La Plaza, Katipunan Avenue): ")
            orders = system.view_orders(branch_name)
            if orders:
                for order in orders:
                    print(f"Order ID: {order['id']}, Customer ID: {order['customer_id']}, Items: {order['items']}, Total Price: {order['total_price']}, Status: {order['status']}")
            else:
                print("No orders found for this branch.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
