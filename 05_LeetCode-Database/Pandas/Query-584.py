import pandas as pd
# Dataframe
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:

    filtered_customers = customer[
        (customer['referee_id'].isnull()) | (customer['referee_id'] != 2)
    ]
    
    result = filtered_customers[['name']]
    
    return result    