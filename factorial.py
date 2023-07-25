def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the given integer.
    """
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
