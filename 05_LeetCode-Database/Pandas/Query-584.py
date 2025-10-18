import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame based on the conditions
    filtered_customers = customer[
        (customer['referee_id'].isnull()) | (customer['referee_id'] != 2)
    ]
    
    # Select only the 'name' column
    result = filtered_customers[['name']]
    
    return result    