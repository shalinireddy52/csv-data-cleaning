import pandas as pd
import logging

# Configure the logger
logging.basicConfig(filename='data_cleaning.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data loaded from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        raise


def handle_missing_data(df):
    logging.info("Handling missing data...")

    # Fill missing 'Date' with today's date
    df['Date'] = df['Date'].fillna(pd.to_datetime('today').strftime('%Y-%m-%d'))

    # Fill missing 'Amount' with the mean value
    df['Amount'] = df['Amount'].fillna(df['Amount'].mean())

    logging.info("Missing data handled.")
    return df


def handle_invalid_data(df):
    logging.info("Handling invalid data...")

    # Convert negative 'Amount' values to absolute values
    df['Amount'] = df['Amount'].apply(lambda x: abs(x))

    logging.info("Invalid data handled.")
    return df


def format_data_types(df):
    logging.info("Formatting data types...")

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Ensure 'Amount' is float
    df['Amount'] = df['Amount'].astype(float)

    logging.info("Data types formatted.")
    return df


def save_cleaned_data(df, output_file):
    try:
        df.to_csv(output_file, index=False)
        logging.info(f"Cleaned data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving cleaned data to {output_file}: {e}")
        raise


def main():
    try:
        # Load raw data
        df = load_data('raw_data.csv')

        # Clean the data
        df = handle_missing_data(df)
        df = handle_invalid_data(df)
        df = format_data_types(df)

        # Save cleaned data to a new file
        save_cleaned_data(df, 'cleaned_data.csv')
        print("Data cleaned and saved to 'cleaned_data.csv'")

    except Exception as e:
        logging.error(f"Error during the data cleaning process: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
