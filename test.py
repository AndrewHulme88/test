def remove_characters(input_string, n):
    # Create a new variable to store the modified string
    modified_string = ""
    # Check if n is less than or equal to 0 or greater than the length of the input string
    if n <= 0 or n > len(input_string):
        modified_string = input_string
    else:
        # If n is positive and less than or equal to the length of the input string, remove the first n characters from the input string and store it in the modified_string.
        modified_string = input_string[n:]

    print(modified_string)

#Example usage:
test_string = "Hello World"
remove_characters(test_string, 3)
