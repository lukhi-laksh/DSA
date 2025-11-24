import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([
        {
        'product_id': row.product_id,
        'store': c,
        'price': row[c],
        }
        for (_, row), (_, mask) in zip(products.iterrows(), products.isna().iterrows())
        for c in [s for s in products.columns if 'store' in s] if not mask[c]])