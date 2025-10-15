# 1 Employee class with instance & class method
class Employee:
    total_employees = 0  # class variable to track total employees

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1  # increase count when object created

    def display_details(self):  # instance method
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_count(cls):  # class method
        print(f"Total Employees: {cls.total_employees}")


# Check Employee class
print("Employees Data ")
e1 = Employee("Ayaz Ali", 50000)
e2 = Employee("Sajad Ali", 60000)
e1.display_details()
e2.display_details()
Employee.total_count()


#  2 Math class with static method to check prime
class Math:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


# Check Math class
print("\nPrime Number checking:")
print("5 is prime:", Math.is_prime(5))
print("88 is prime:", Math.is_prime(88))


# 3 Account class using @property and @setter
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount


# Check Account class
print("\nAccount test:")
acc = Account(1000)
print("Current Balance:", acc.balance)
acc.balance = 2000
print("Updated Balance:", acc.balance)
acc.balance = -500  # invalid


# 4 Book class with __init__ and multiple objects
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"'{self.title}' by {self.author}, Price: {self.price}")


# Check Book class
print("\nBooks Information :")
b1 = Book("Python Basics to Advance", "Maqsood Ahmed", 5000)
b2 = Book("How to program java ","Ayaz Ali", 5500)
b3 = Book("Data Science and ML", "Syed Asad Ali", 4500)

b1.display()
b2.display()
b3.display()
