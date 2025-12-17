import pandas as pd
from datetime import datetime

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:

    d = datetime(2019,8,16)

    temp = (
        products
        .loc[products.change_date <= d]
        .groupby('product_id', as_index=False)
        .apply(lambda g: g.sort_values('change_date').iloc[-1,:])
        .rename(columns = {'new_price':'price'})
    )

    left_out = set(products.product_id) - (set(products.product_id) & set(temp.product_id))

    temp2 = pd.DataFrame({'product_id': list(left_out), 'price': [10]*len(list(left_out))})

    return pd.concat([temp, temp2], axis=0)[['product_id','price']]
    