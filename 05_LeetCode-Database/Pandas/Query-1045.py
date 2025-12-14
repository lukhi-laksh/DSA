import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_products = len(product)
    get_customer_counts = customer.groupby('customer_id')['product_key'].nunique().reset_index(name = 'num_products')
    result = get_customer_counts[get_customer_counts['num_products'] == total_products ].drop(columns = 'num_products')
    return result