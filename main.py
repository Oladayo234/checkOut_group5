from src.models.check_out.Attendant import Attendant
from src.models.check_out.Cart import Cart
from src.models.check_out.Invoice import Invoice
from src.models.check_out.Product import Product


def main():
    cart = Cart()
    attendant_name = input("Enter attendant name: ")
    try:
        attendant = Attendant(attendant_name)
    except ValueError as e:
        print("Error:", e)
        return

    while True:
        print("\n===== CHECKOUT SYSTEM =====")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. View cart")
        print("4. Generate invoice")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Enter product name: ")

            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter quantity: "))

                product = Product(name, price, quantity)
                cart.add_product_to_cart(product)

                print(f"{name} added to cart")

            except ValueError as e:
                print("Error:", e)


        elif choice == "2":
            name = input("Enter product name to remove: ")

            dummy_product = Product(name, 0, 0)

            try:
                message = cart.remove_product_from_cart(dummy_product)
                print(message)
            except ValueError as e:
                print("Error:", e)


        elif choice == "3":
            if not cart.products:
                print("Cart is empty")
            else:
                print("\nCart contents:")
                for product in cart.products:
                    print(f"{product.name} - Price: {product.price}, Quantity: {product.quantity}")


        elif choice == "4":
            try:
                invoice = Invoice(cart)
                attendant.invoices.append(invoice)

                print("\n===== RECEIPT =====")
                print(invoice.get_receipt())

            except ValueError as e:
                print("Error:", e)


        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()