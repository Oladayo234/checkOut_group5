class Product:
    def __init__(self, name, price, quantity):
        self.name = self.__validate_name(name)
        self.price = self.__validate_price(price)
        self.quantity = self.__validate_quantity(quantity)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = self.__validate_name(name)

    def set_price(self, price):
        self.price = self.__validate_price(price)

    def set_quantity(self, quantity):
        self.quantity = self.__validate_quantity(quantity)

    def __validate_price(self, price):
        validate_numeric_value = self.__validate_numeric_value(price)
        if validate_numeric_value < 0:
            raise ValueError("Price cannot be negative")
        return price

    def __validate_quantity(self, quantity):
        validate_numeric_value = self.__validate_numeric_value(quantity)
        if validate_numeric_value < 0:
            raise ValueError("Quantity cannot be negative")
        return quantity

    def __validate_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty")
        return name

    def __validate_numeric_value(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a digit")
        return (value)




