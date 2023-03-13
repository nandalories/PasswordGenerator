import pandas as pd

def parse_csv(filename):
    data = pd.read_csv(filename)
    # Example operations
    sorted_data = data.sort_values('column_name')
    filtered_data = data[data['column_name'] > 0]
    aggregated_data = data.groupby('column_name').sum()
    # Export results
    sorted_data.to_csv('sorted_data.csv')
    filtered_data.to_excel('filtered_data.xlsx')
    aggregated_data.to_json('aggregated_data.json')
