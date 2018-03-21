import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset.csv")

# Calculate Gain of "Education"
print("Confusion Matrix of Education")
print(df.groupby("national_rank").size())   
plt.show()
