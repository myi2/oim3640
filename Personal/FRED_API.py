import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch data from FRED
def fetch_fred_data(series_id, api_key):
    base_url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    response = requests.get(base_url)
    data = response.json()['observations']
    df = pd.DataFrame(data)
    # Convert date string to datetime and set as index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

# Function for basic EDA
def basic_eda(df):
    print(df.describe())
    # Histograms or box plots
    df.plot(kind='hist')
    plt.show()
    # Time series plot
    df.plot()
    plt.show()

# Example usage
api_key = 'ef876b4d890878b2c3c3b68a7f3db58f'
series_ids = ['UNRATE', 'GDP']  # Example series IDs for unemployment rate and GDP
dfs = {}
for series_id in series_ids:
    dfs[series_id] = fetch_fred_data(series_id, api_key)
    basic_eda(dfs[series_id])

# Further analysis as needed
