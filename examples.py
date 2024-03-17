from callback import callback_factory, CallbackFactory

# ******* CallbackFactory examples *******
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

callback = CallbackFactory(greet, "Alice", greeting="Hi")

# normal calling
print(callback())  # Output: Hi, Alice!

# calling with partial arguments override
print(callback(greeting="Heyaa")) # Output: Heyaa, Alice!

# calling with arguments override
print(callback(name="Chris", greeting="Hola")) # Output: Hola, Chris!

# using a lambda function
callback = CallbackFactory(lambda x, y: x ** y, 2, 3)
print(callback())  # Output: 8

# calling with arguments override
print(callback(x=4, y=2))  # Output: 16


# ******* callback_factory examples *******
def add(a, b=3):
    return a + b

callback = callback_factory(add, 3, b=4)

# normal calling
print(callback())  # Output: 7

# calling with partial arguments override
print(callback(a=8))  # Output: 12

# calling with arguments override
print(callback(a=2, b=7))  # Output: 9

# using a lambda function
callback = callback_factory(lambda x, y: x ** y, 2, 3)
print(callback())  # Output: 8

# calling with arguments override
print(callback(x=4, y=2))  # Output: 16
