
import pandas as pd

# Load the dataset
file_path = 'hot100.csv'  # Path to your Billboard Hot 100 dataset
billboard = pd.read_csv(file_path)

# Ensure the 'Song' column is treated as text
billboard['Song'] = billboard['Song'].astype(str)

# Convert the 'Date' column to datetime
billboard['Date'] = pd.to_datetime(billboard['Date'], errors='coerce')

# Filter the data for years 2010-2024
billboard = billboard[billboard['Date'].dt.year.between(2010, 2024)]

# Drop rows with missing values in essential columns
billboard = billboard.dropna(subset=['Date', 'Rank', 'Song', 'Artist'])

# Ensure proper data types
billboard['Rank'] = pd.to_numeric(billboard['Rank'], errors='coerce', downcast='integer')
billboard['Song'] = billboard['Song'].str.strip()
billboard['Artist'] = billboard['Artist'].str.strip()

# Sort the data chronologically by 'Date'
billboard = billboard.sort_values(by='Date')

# Reset the index after sorting (optional)
billboard = billboard.reset_index(drop=True)

# Group by Song Title and summarize the data
billboard_summary = billboard.groupby('Song').agg({
    'Rank': ['mean', 'min'],  # Average and Best Rank
    'Date': 'count'           # Total Weeks on Chart
}).reset_index()

# Rename the columns for easier interpretation
billboard_summary.columns = ['Song', 'Avg Rank', 'Best Rank', 'Weeks on Chart']

# Save the preprocessed data to a new CSV file
output_path = 'correlation_billboard_preprocessed.csv'  # This will save it in the same directory as 'hot100.csv'
billboard_summary.to_csv(output_path, index=False)

print(f"Preprocessed dataset saved to: {output_path}")
