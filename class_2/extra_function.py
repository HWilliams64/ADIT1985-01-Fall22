# This is a single line
"""
This is a single line
This is another ling
"""

def my_function(arg_1:str) -> str:
    """
    This function adds "some text" to arg_1

    Args:
        arg_1 (str): This is any text

    Returns:
        str: The text inputted plus "some text"
    """
    
    return arg_1 + " some text"

print(my_function("12"))