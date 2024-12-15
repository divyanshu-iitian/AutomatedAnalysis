# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "seaborn", "matplotlib", "openai"]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai

# Ensure the AIPROXY_TOKEN is set
AIPROXY_TOKEN = os.environ.get("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable not set.")
    sys.exit(1)

openai.api_key = AIPROXY_TOKEN

def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print(f"Loaded {filename} successfully.")
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def analyze_rating_distribution(df):
    # Plot rating distribution based on the 'average_rating' column
    plt.figure(figsize=(8, 6))
    sns.histplot(df['average_rating'], bins=20, kde=True)
    plt.title('Distribution of Average Ratings')
    plt.xlabel('Average Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig("rating_distribution.png")
    plt.show()

def analyze_correlation_matrix(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    # Generate a correlation matrix of numeric columns
    corr = numeric_df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Numeric Features')
    plt.tight_layout()
    plt.savefig("correlation_matrix.png")
    plt.show()


def generate_readme(df):
    # Generate basic insights for the README file
    insights = f"# Data Analysis Insights\n\n"
    insights += f"### Dataset Overview\n\n"
    insights += f"Number of records: {len(df)}\n"
    insights += f"Columns: {', '.join(df.columns)}\n"
    
    # Average rating insights
    avg_rating = df['average_rating'].mean()
    insights += f"\n### Average Rating Insights\n"
    insights += f"The average rating across all books is {avg_rating:.2f}.\n"

    # Highest-rated books
    highest_rated = df[['title', 'average_rating']].sort_values(by='average_rating', ascending=False).head(5)
    insights += f"\n### Top 5 Highest-Rated Books\n"
    for idx, row in highest_rated.iterrows():
        insights += f"{row['title']} - {row['average_rating']:.2f}\n"
    
    # Save the insights to a README file
    with open("README.md", "w") as f:
        f.write(insights)

def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        print("Error: Input file must be a CSV.")
        sys.exit(1)

    # Load dataset
    df = load_data(filename)

    # Perform analysis and generate insights
    analyze_rating_distribution(df)
    analyze_correlation_matrix(df)
    generate_readme(df)

if __name__ == "__main__":
    main()
