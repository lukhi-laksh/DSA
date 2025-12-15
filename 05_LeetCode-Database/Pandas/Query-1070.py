import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales['minyear'] = sales.groupby('product_id')['year'].transform(lambda x : x.min())
    return sales[sales['year']==sales['minyear']][['product_id', 'minyear', 'quantity', 'price']].rename(columns={'minyear':'first_year'})