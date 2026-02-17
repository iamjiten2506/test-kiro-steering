def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def calculate(a, b, operation):
    """Perform calculation based on operation.
    
    Args:
        a: First number
        b: Second number
        operation: Operation to perform (+, -, *, /)
        
    Returns:
        Result of the calculation
        
    Raises:
        ValueError: If operation is invalid
        ZeroDivisionError: If dividing by zero
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Invalid operation: {operation}")
