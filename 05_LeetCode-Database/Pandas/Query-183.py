import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=customers.merge(orders,how='left',left_on='id',right_on='customerId')[['name','customerId']]
    df=df[df['customerId'].isna()]
    return df[['name']].rename(columns={'name':'customers'})