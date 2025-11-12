import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    df = visits.merge(transactions, how = 'left')
    
    return (df[df.transaction_id.isnull()]
                 .groupby('customer_id')['visit_id'].agg(
                          count_no_trans = 'size').reset_index())
                 