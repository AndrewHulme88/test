import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(42)
num_samples = 100

# Generate random data
data = {
    'Feature1': np.random.randint(0, 100, size=num_samples),
    'Feature2': np.random.uniform(0, 1, size=num_samples),
    'Feature3': np.random.choice(['A', 'B', 'C'], size=num_samples),
    'Stolen': np.random.choice([0, 1], size=num_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('cwdata_cleaned.csv', index=False)

print("Sample CSV file 'cwdata_cleaned.csv' has been created.")
