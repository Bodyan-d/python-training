class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_email(self, new_email):
        self.email = new_email

    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self._quantity = quantity

    def get_price(self):
        return self.price

    def buy(self, amount):
        if amount > self._quantity or amount <= 0:
            return False

        self._quantity -= amount
        return True

    def restock(self, amount):
        if amount <= 0:
            return False

        self._quantity += amount
        return True
        

user = User("john", "john@mail.com", "1234")
print(user.get_info())
print(user.check_password("1234"))

product = Product("Laptop", 1200, 5)
product.buy(2)
product.restock(3)