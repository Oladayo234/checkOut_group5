from src.models.check_out.Attendant import Attendant
from src.models.check_out.Cart import Cart
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
        print("5. View pending invoices")
        print("6. Process payment for invoice")
        print("7. Exit")

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
            item = Product(name, 0, 0)
            try:
                message = cart.remove_product_from_cart(item)
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
                invoice = attendant.create_invoice(cart)
                print("\n===== INVOICE =====")
                print(invoice.get_invoice())
                
                payment_confirm = input("\nConfirm payment? (y/n): ").lower()
                if payment_confirm == 'y':
                    paid_invoice = attendant.process_payment(invoice.id)
                    print("\n===== RECEIPT =====")
                    print(paid_invoice.get_receipt())
                    
                    cart.products.clear()
                    print("\nTransaction completed successfully!")
                else:
                    print("Payment cancelled. Invoice saved for later.")

            except (ValueError, TypeError) as e:
                print("Error:", e)


        elif choice == "5":
            unpaid_invoices = attendant.get_unpaid_invoices()
            if not unpaid_invoices:
                print("No pending invoices")
            else:
                print("\n===== PENDING INVOICES =====")
                for invoice in unpaid_invoices:
                    print(f"Invoice #{invoice.id} - Total: N{invoice.calculate_total():.2f}")


        elif choice == "6":
            try:
                invoice_id = int(input("Enter invoice ID to process payment: "))
                paid_invoice = attendant.process_payment(invoice_id)
                print("\n===== RECEIPT =====")
                print(paid_invoice.get_receipt())
                print("\nPayment processed successfully!")
            except (ValueError, TypeError) as e:
                print("Error:", e)


        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()