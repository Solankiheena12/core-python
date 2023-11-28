# Encapsulation is one of the fundamental concepts in object-oriented programming

# Encapsulation hides the internal details of an object and restricts access to the inner workings of the object.

class Example:
    def __init__(self):
        self.value = 10

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        if new_value < 5:
            self.value = new_value
            print("Congo")
        else:
            print("Invalid value. Value must be non-negative.")



example_instance = Example()

# Using setter method
# example_instance.set_value(3)  # Output: 3
example_instance.set_value(2)  # Output: Invalid value. Value must be non-negative.

# Using getter method
print(example_instance.get_value())  # Output: 3