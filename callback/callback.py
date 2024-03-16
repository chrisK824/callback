from functools import wraps
from typing import Callable


class CallbackFactory():
    def __init__(self, func: Callable, *args, **kwargs):
        """
        Initialize the CallbackFactory.

        Parameters:
            func (Callable): The callable function to be wrapped.
            *args: Positional arguments to be passed to the function.
            **kwargs: Keyword arguments to be passed to the function.

        Raises:
            TypeError: If `func` is not a callable object.
        """
        if not callable(func):
            raise TypeError("The 'func' argument must be callable")
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, *override_args, **override_kwargs):
        """
        Call the wrapped function with provided arguments.
        If no arguments are provided during calling, 
        then the stored ones (during instance creation) are used.

        Returns:
            The result of calling the wrapped function with provided arguments.
        """
        runtime_args = override_args if override_args else self.args
        runtime_kwargs = override_kwargs if override_kwargs else self.kwargs

        return self.func(*runtime_args, **runtime_kwargs)


def callback_factory(func: Callable, *args, **kwargs):
    """
    Create a callback function that wraps the provided callable function.

    Parameters:
        func (Callable): The callable function to be wrapped.
        *args: Positional arguments to be passed to the function.
        **kwargs: Keyword arguments to be passed to the function.

    Returns:
        A wrapped function that calls the provided callable function with the specified arguments.

    Raises:
        TypeError: If `func` is not a callable object.
    """
    if not callable(func):
        raise TypeError("The 'func' argument must be callable")
    @wraps(func)
    def wrapped_func(*override_args, **override_kwargs):
        runtime_args = override_args if override_args else args
        runtime_kwargs = override_kwargs if override_kwargs else kwargs
        return func(*runtime_args, **runtime_kwargs)
    return wrapped_func
