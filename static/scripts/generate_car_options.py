"""
Script to extract unique car models from the dataset and generate HTML select options
"""

import pandas as pd
import os

# Read the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
csv_path = os.path.join(project_dir, 'Notebook', 'cars.csv')

# Read the CSV file
df = pd.read_csv(csv_path)

# Get unique car names
unique_car_names = sorted(df['name'].unique())

# Generate HTML options
options_html = ""
for name in unique_car_names:
    options_html += f'<option value="{name}">{name}</option>\n'

# Print the HTML options for copy-pasting into the template
print("<!-- Car model options -->")
print(options_html)
