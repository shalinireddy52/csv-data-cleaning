from datetime import datetime
import pytz


def handle_missing_data(df):
    logging.info("Handling missing data...")

    # Fill missing 'Date' with today's date in a specific timezone (e.g., UTC)
    timezone = pytz.timezone("UTC")
    current_time = datetime.now(timezone)
    df['Date'] = df['Date'].fillna(current_time.strftime('%Y-%m-%d'))

    # Fill missing 'Amount' with the mean value
    df['Amount'] = df['Amount'].fillna(df['Amount'].mean())

    logging.info("Missing data handled.")
    return df


def format_data_types(df):
    logging.info("Formatting data types...")

    # Convert 'Date' to datetime (this will handle various date formats)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Coerce invalid dates to NaT (Not a Time)

    # Handle invalid date entries (if any)
    invalid_dates = df[df['Date'].isna()]
    if not invalid_dates.empty:
        logging.warning(f"Invalid dates found: {invalid_dates}")

    # Ensure 'Amount' is float
    df['Amount'] = df['Amount'].astype(float)

    logging.info("Data types formatted.")
    return df
