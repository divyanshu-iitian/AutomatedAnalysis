# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "seaborn", "matplotlib", "openai", "os"]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai

# Ensure the AIPROXY_TOKEN is set
AIPROXY_TOKEN = os.environ.get("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDE0OTZAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.Awu2CaegqXKp1WaU9cZGoWXzIn53SkKl8cuhSeDei1c")
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable not set.")
    sys.exit(1)

openai.api_key = AIPROXY_TOKEN

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        print("Error: Input file must be a CSV.")
        sys.exit(1)

    try:
        # Load dataset
        df = pd.read_csv(filename)
        print(f"Loaded {filename} successfully.")
        # Your analysis functions go here
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
