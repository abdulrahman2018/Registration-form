import pandas as pd
import random
from datetime import datetime, timedelta

def generate_random_stock_data(num_entries=1000, num_companies=5):
    start_date = datetime(2023, 1, 1)
    data = []

    for _ in range(num_entries):
        date = start_date.strftime('%Y-%m-%d')
        for company_id in range(1, num_companies + 1):
            company = f"Company-{company_id}"
            open_price = round(random.uniform(100, 5000), 2)
            close_price = round(random.uniform(100, 5000), 2)
            high_price = max(open_price, close_price, round(random.uniform(100, 5000), 2))
            low_price = min(open_price, close_price, round(random.uniform(100, 5000), 2))

            data.append([date, company, open_price, close_price, high_price, low_price])

        start_date += timedelta(days=1)

    return data

def main():
    num_entries = 1000  # Change this to the desired number of entries
    num_companies = 5   # Change this to the desired number of companies

    data = generate_random_stock_data(num_entries, num_companies)
    df = pd.DataFrame(data, columns=["Date", "Company", "Open", "Close", "High", "Low"])

    csv_filename = "stock_data.csv"
    df.to_csv(csv_filename, index=False)

if __name__ == "__main__":
    main()
