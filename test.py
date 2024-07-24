def calculate_area(shape, dimensions):
    """
    Calculate the area of a given shape based on user input.

    Parameters:
    shape (str): The shape for which to calculate the area. Can be 'circle', 'rectangle', or 'triangle'.
    dimensions (list): A list of dimensions for the shape. The length and order of the list depend on the shape:
        - For a circle, the list should contain one number: the radius.
        - For a rectangle, the list should contain two numbers: the length and the width.
        - For a triangle, the list should contain three numbers: the base, the height, and the third side length.

    Returns:
    float: The area of the shape.
    """

    # Calculate the area based on the shape
    if shape.lower() == 'circle':
        # Area of a circle is calculated using the formula πr²
        area = 3.14159 * (dimensions[0] ** 2)
    elif shape.lower() == 'rectangle':
        # Area of a rectangle is calculated using the formula lw
        area = dimensions[0] * dimensions[1]
    elif shape.lower() == 'triangle':
        # Area of a triangle is calculated using the formula 1/2bh
        area = 0.5 * dimensions[0] * dimensions[1]
    else:
        # If the shape is not recognized, raise an error
        raise ValueError(f"Invalid shape '{shape}'. Supported shapes are 'circle', 'rectangle', and 'triangle'.")

    return area

# Example for a circle with radius 5
print(calculate_area('circle', [5]))

# Example for a rectangle with length 4 and width 6
print(calculate_area('rectangle', [4, 6]))

# Example for a triangle with base 5, height 7, and third side length 8
print(calculate_area('triangle', [5, 7, 8]))
