
# Coding Exercise: Decoding a Secret Message
# In this exercise, you will write code to solve a problem. Your code must be in either Python or JavaScript—solutions in other languages will not be accepted! You can write your code using any IDE you want.

# Problem
# You are given a Google Doc like this one that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

# The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

# The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

# Any positions in the grid that do not have a specified character should be filled with a space character.

# You can assume the document will always have the same format as the example document linked above.

# For example, the simplified example document linked above draws out the letter 'F':

# █▀▀▀
# █▀▀ 
# █   
# Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

# Specifications
# Your code must be written in Python (preferred) or JavaScript.

# You may use external libraries.

# You may write helper functions, but there should be one function that:

# 1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

# 2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.






import requests
import re
from bs4 import BeautifulSoup

def decode_secret_message(url):
    # Get the content of the Google Doc URL
    response = requests.get(url)
    
    # Ensure that the request was successful
    if response.status_code != 200:
        print("Error: Unable to fetch the document.")
        return
    
    # Extract the content of the document as HTML
    doc_content = response.text
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(doc_content, 'html.parser')
    
    # # Print the first 500 characters of the document for debugging
    # print("Document Content Preview:")
    # print(soup.prettify()[:500])  # Preview first 500 characters of the content
    
    # Look for the table containing the grid data (adjust the selector if needed)
    table = soup.find('table')
    
    if not table:
        print("Error: No table found in the document.")
        return
    
    # Parse the rows of the table
    rows = table.find_all('tr')
    
    # List to store the extracted data
    matches = []
    
    for row in rows:
        cells = row.find_all('td')
        
        # Ensure we have the right number of cells (x, character, y)
        if len(cells) == 3:
            x = cells[0].get_text(strip=True)
            char = cells[1].get_text(strip=True)
            y = cells[2].get_text(strip=True)
            
            # Validate the extracted data
            if x.isdigit() and y.isdigit():
                matches.append((int(x), char, int(y)))
    
    # # Print matches for debugging
    # print("\nMatches Found:")
    # print(matches)
    
    # If no data found, print an error
    if not matches:
        print("Error: No valid data found.")
        return
    
    # Create a dictionary to store grid coordinates and characters
    grid_dict = {}
    
    # Fill the grid_dict with the coordinates and characters
    for x, char, y in matches:
        grid_dict[(x, y)] = char
    
    # # Debugging the grid_dict
    # print("\nGrid Dictionary:")
    # print(grid_dict)
    
    # Determine the grid size
    max_x = max([coord[0] for coord in grid_dict.keys()])
    max_y = max([coord[1] for coord in grid_dict.keys()])
    
    # Create a grid with spaces as placeholders
    grid = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    
    # Populate the grid with the characters
    for (x, y), char in grid_dict.items():
        grid[x][y] = char
    
    # Print the grid
    # print("\nDecoded Grid:")
    for row in grid:
        print("".join(row))

# URL of the Google Doc containing the grid data
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode_secret_message(url)
