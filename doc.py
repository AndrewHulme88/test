import requests
from bs4 import BeautifulSoup
import re

def fetch_document(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator='\n')


    # Extract relevant content based on known headings
    start_marker = 'x-coordinate'
    end_marker = 'Coding assessment input data example'
    start_index = text.find(start_marker)
    end_index = text.find(end_marker, start_index)

    if start_index != -1 and end_index != -1:
        relevant_text = text[start_index:end_index].strip()
    else:
        relevant_text = text

    return relevant_text

def parse_data(document):
    pattern = re.compile(r'(\d+)\s+(\S)\s+(\d+)')
    matches = pattern.findall(document)
    data = [(int(x), char, int(y)) for x, char, y in matches]
    return data

def create_grid(data):
    if not data:
        return []

    # Determine grid size
    max_x = max(x for x, char, y in data)
    max_y = max(y for x, char, y in data)

    # Create the grid with padding for better readability
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with characters based on coordinates
    for x, char, y in data:
        grid[y][x] = char

    # Invert the grid
    grid.reverse()

    return grid

def print_grid(grid):
    # Print the grid with proper formatting
    for row in grid:
        print(''.join(row))

def decode_message(url):
    text = fetch_document(url)
    data = parse_data(text)
    grid = create_grid(data)
    print_grid(grid)

# Example usage:
decode_message('https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub')
