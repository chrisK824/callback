# callback
Callback factory in Python, providing two similar approaches to produce parameterized and flexible callbacks that can be overriden during execution.

## Installation

`pip install callback-factory`

## Example

```
from callback import CallbackFactory

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

callback = CallbackFactory(greet, "Alice", greeting="Hi")

print(callback())  # Output: Hi, Alice!
```
One can find more usage examples in `examples.py` at the root folder of this project.