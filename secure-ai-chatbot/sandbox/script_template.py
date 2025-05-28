# sandbox/script_template.py
import pandas as pd
import matplotlib.pyplot as plt

# Data load
file_path = "{file_path}"
data = pd.read_csv(file_path)

# Analysis block
{code}

# Save output
plt.savefig("output.png")
