import math

def calculate_area(shape, *dimensions):
    """
    This function calculates the area of different geometric shapes based on the user's input.
    The function takes the shape type as the first argument and the necessary dimensions as variable arguments.

    Args:
        shape (str): The type of shape for which the area is to be calculated. Valid shapes are 'circle', 'rectangle', and 'triangle'.
        *dimensions (float or int): The dimensions required for calculating the area of the specified shape. The number of dimensions depends on the shape.

    Raises:
        ValueError: If the shape type is not 'circle', 'rectangle', or 'triangle'.
        ValueError: If the number of dimensions provided is incorrect for the given shape.

    Returns:
        float: The calculated area of the specified shape.
    """
    if shape == "circle":
        # Check if exactly one dimension (radius) is provided for a circle.
        if len(dimensions) != 1:
            raise ValueError("For a circle, exactly one dimension (radius) is required.")
        radius = dimensions[0]
        return math.pi * radius * radius
    elif shape == "rectangle":
        # Check if exactly two dimensions (length and width) are provided for a rectangle.
        if len(dimensions) != 2:
            raise ValueError("For a rectangle, exactly two dimensions (length and width) are required.")
        length = dimensions[0]
        width = dimensions[1]
        return length * width
    elif shape == "triangle":
        # Check if exactly three dimensions (base and height) are provided for a triangle.
        if len(dimensions) != 2:
            raise ValueError("For a triangle, exactly two dimensions (base and height) are required.")
        base = dimensions[0]
        height = dimensions[1]
        return 0.5 * base * height
    else:
        raise ValueError(f"Invalid shape type. Valid shapes are 'circle', 'rectangle', and 'triangle'.")

# Examples of how to call the function for each shape type:
# Calculating the area of a circle:
try:
    radius = float(input("Enter the radius of the circle: "))
    circle_area = calculate_area("circle", radius)
    print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")
except ValueError as ve:
    print(f"Error: {ve}")

# Calculating the area of a rectangle:
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle_area = calculate_area("rectangle", length, width)
    print(f"The area of the rectangle with length {length} and width {width} is: {rectangle_area:.2f}")
except ValueError as ve:
    print(f"Error: {ve}")

# Calculating the area of a triangle:
try:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triangle_area = calculate_area("triangle", base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {triangle_area:.2f}")
except ValueError as ve:
    print(f"Error: {ve}")
