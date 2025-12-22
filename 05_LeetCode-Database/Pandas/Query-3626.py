import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    return (
        inventory
            .loc[inventory.groupby("store_id")["product_name"].transform("count") >= 3, ["store_id", "product_name", "quantity", "price"]]
            .assign(
                max_price=lambda df: df.groupby("store_id")["price"].transform("max"),
                min_price=lambda df: df.groupby("store_id")["price"].transform("min"),
                most_exp_product=lambda df: df.loc[df["max_price"] == df["price"], ["product_name"]],
                cheapest_product=lambda df: df.loc[df["min_price"] == df["price"], ["product_name"]]
                )
            .dropna(subset=['most_exp_product', 'cheapest_product'], how='all')
            .sort_values(["store_id", "price"], ascending=[1, 0])
            .assign(imbalance_check=lambda df: df.groupby("store_id")["quantity"].transform("diff"))
            .groupby("store_id", as_index=False)
            .agg(
                most_exp_product=("most_exp_product", "first"),
                cheapest_product=("cheapest_product", "first"),
                imbalance_check=("imbalance_check", "first"),
                imbalance_ratio=("quantity", lambda c: round(c.max() / c.min(), 2))
            )
            .merge(stores, on="store_id")
            .loc[lambda df: df["imbalance_check"] > 0, ["store_id", "store_name", "location", "most_exp_product", "cheapest_product", "imbalance_ratio"]]
            .sort_values(["imbalance_ratio", "store_name"], ascending=[0, 1])
    )