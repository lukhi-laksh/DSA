import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    merged = products.merge(orders)[['product_name','unit','order_date']]

    feb = merged[
        (merged.order_date.dt.year == 2020) &
        (merged.order_date.dt.month == 2)
    ]
    
    ans = feb.groupby('product_name')['unit'].sum().reset_index()

    return ans[ans.unit>=100]