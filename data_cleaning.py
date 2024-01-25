import pandas as pd


# Step 1: Load Data
def load_data(file_path):
    return pd.read_csv(file_path)


# Step 2: Handle Missing Data
def handle_missing_data(df):
    # Fill missing 'Date' with today's date
    df['Date'] = df['Date'].fillna(pd.to_datetime('today').strftime('%Y-%m-%d'))

    # Fill missing 'Amount' with the mean value or zero
    df['Amount'] = df['Amount'].fillna(df['Amount'].mean())

    return df


# Step 3: Handle Invalid Data
def handle_invalid_data(df):
    # Convert negative 'Amount' values to absolute values
    df['Amount'] = df['Amount'].apply(lambda x: abs(x))

    return df


# Step 4: Format Data Types
def format_data_types(df):
    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Ensure 'Amount' is float
    df['Amount'] = df['Amount'].astype(float)

    return df


# Step 5: Save Cleaned Data
def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)


def main():
    # Load raw data
    df = load_data('raw_data.csv')

    # Clean the data
    df = handle_missing_data(df)
    df = handle_invalid_data(df)
    df = format_data_types(df)

    # Save cleaned data to a new file
    save_cleaned_data(df, 'cleaned_data.csv')
    print("Data cleaned and saved to 'cleaned_data.csv'")


if __name__ == "__main__":
    main()
