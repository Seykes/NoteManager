"""
Module for storage wrapping functions
"""


import functools


def with_str(string):
    """
    Wrapper function for create __str__ return type in functions
    """
    def wrapper (f):
        class FuncType:
            def __call__ (self, *args, **kwargs):
                # call the original function
                return f(*args, **kwargs)
            def __str__ (self):
                # call the custom __str__ function
                return string

        # decorate with functool.wraps to make the resulting function appear like f
        return functools.wraps(f)(FuncType())
    return wrapper
